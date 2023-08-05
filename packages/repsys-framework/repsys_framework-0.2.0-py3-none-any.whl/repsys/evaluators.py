import logging
from typing import Dict, Optional, Any, Callable

import pandas as pd
import pymde
from pandas import DataFrame
from scipy.sparse import issparse
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import pairwise_distances

from repsys.dataset import Dataset
from repsys.helpers import *
from repsys.metrics import *
from repsys.model import Model

logger = logging.getLogger(__name__)


def embeddings_to_df(embeds: ndarray, ids: ndarray) -> DataFrame:
    df = pd.DataFrame({"id": ids, "x": embeds[:, 0], "y": embeds[:, 1]})
    return df


def results_to_df(results: Dict[str, ndarray], ids: List[str]) -> DataFrame:
    df = pd.DataFrame({"id": ids, **results})
    return df


def write_df(df: DataFrame, file_name: str, index: bool = False) -> None:
    df.to_csv(os.path.join(tmp_dir_path(), file_name), index=index)


def read_df(file_path: str, index_col: str = None) -> DataFrame:
    if index_col is not None:
        return pd.read_csv(file_path, dtype={index_col: str}).set_index(index_col)
    else:
        return pd.read_csv(file_path, index_col=0)


def print_results(results: List[DataFrame]):
    for i, df in enumerate(results[-2:]):
        if i == 0 and len(results) > 1:
            print("-> Previous results:")
        else:
            print("-> Current results:")
        print(df.describe())
        print("\n")


def sort_partially(X: ndarray, k: int) -> ndarray:
    row_indices = np.arange(X.shape[0])[:, np.newaxis]
    top_k_indices = np.argpartition(X, k, axis=1)[:, :k]
    top_k_predicts = X[row_indices, top_k_indices]
    sorted_indices = np.argsort(top_k_predicts, axis=1)
    return top_k_indices[row_indices, sorted_indices]


class ModelEvaluator:
    def __init__(
        self,
        dataset: Dataset,
        rp_k: List[int] = None,
        ndcg_k: List[int] = None,
        coverage_k: List[int] = None,
        diversity_k: List[int] = None,
        novelty_k: List[int] = None,
    ):
        if rp_k is None:
            rp_k = [20, 50]

        if ndcg_k is None:
            ndcg_k = [100]

        if coverage_k is None:
            coverage_k = [20, 50]

        if diversity_k is None:
            diversity_k = [5, 10]

        if novelty_k is None:
            novelty_k = [5, 10]

        self.rp_k = rp_k
        self.ndcg_k = ndcg_k
        self.coverage_k = coverage_k
        self.diversity_k = diversity_k
        self.novelty_k = novelty_k

        self.evaluated_models: List[str] = []

        self._dataset = dataset
        self._user_results: Dict[str, List[DataFrame]] = {}
        self._item_results: Dict[str, List[DataFrame]] = {}
        self._summary_results: Dict[str, List[DataFrame]] = {}
        self._version: str = CURRENT_VERSION

    def compute_metrics(
        self, X_predict: ndarray, X_true: ndarray
    ) -> Tuple[Dict[str, float], Dict[str, ndarray], Dict[str, ndarray]]:
        max_k = max(max(self.rp_k), max(self.ndcg_k))

        logger.info(f"Sorting predictions for maximal K={max_k}")
        predict_sort = sort_partially(-X_predict, k=max_k)
        true_sort = sort_partially(-X_true, k=max_k)

        X_train = self._dataset.get_train_data()

        logger.info("Computing item distances")
        X_distances = pairwise_distances(X_train.T, metric="cosine")

        summary_results = {}
        user_results = {}
        item_results = {}

        logger.info("Computing precision and recall")
        precision_dict, recall_dict = dict(), dict()
        for k in self.rp_k:
            precision_dict[k], recall_dict[k] = get_pr(X_predict, X_true, predict_sort, k)

        for k in self.rp_k:
            user_results[f"recall@{k}"] = recall_dict.get(k)
            summary_results[f"recall@{k}"] = recall_dict.get(k).mean()

        logger.info("Computing NDCG")
        for k in self.ndcg_k:
            ndcg = get_ndcg(X_predict, X_true, predict_sort, true_sort, k)
            user_results[f"ndcg@{k}"] = ndcg
            summary_results[f"ndcg"] = ndcg.mean()

        logger.info("Computing diversity")
        for k in self.diversity_k:
            diversity = get_diversity(X_distances, predict_sort, k)
            user_results[f"diversity@{k}"] = diversity
            summary_results[f"diversity@{k}"] = diversity.mean()

        logger.info("Computing novelty")
        for k in self.novelty_k:
            novelty = get_novelty(X_train, predict_sort, k)
            user_results[f"novelty@{k}"] = novelty
            summary_results[f"novelty@{k}"] = novelty.mean()

        for k in self.rp_k:
            user_results[f"precision@{k}"] = precision_dict.get(k)
            summary_results[f"precision@{k}"] = precision_dict.get(k).mean()

        logger.info("Computing MAE, MSE and RMSE")
        mae, mse, rmse = get_accuracy_metrics(X_predict, X_true)
        user_results["mae"], user_results["mse"], user_results["rmse"] = mae, mse, rmse

        logger.info("Computing coverage")
        for k in self.coverage_k:
            coverage = get_coverage(X_predict, predict_sort, k)
            summary_results[f"coverage@{k}"] = coverage

        logger.info("Computing item popularity")
        item_results["popularity"] = get_popularity(X_predict)

        return summary_results, user_results, item_results

    def print(self) -> None:
        for model in self.evaluated_models:
            print(f"Model '{model.upper()}' Evaluation Results:\n")

            print("User Metrics:")
            print_results(self._user_results.get(model))

            print("Item Metrics:")
            print_results(self._item_results.get(model))

    def get_user_results(self, model_name: str) -> Optional[DataFrame]:
        results = self._user_results.get(model_name)
        return results[-1] if results is not None else None

    def get_item_results(self, model_name: str) -> Optional[DataFrame]:
        results = self._item_results.get(model_name)
        return results[-1] if results is not None else None

    def get_prev_summary(self, model_name: str) -> Optional[DataFrame]:
        results = self._summary_results.get(model_name)
        return results[-2] if results is not None and len(results) > 1 else None

    def get_current_summary(self, model_name: str) -> Optional[DataFrame]:
        results = self._summary_results.get(model_name)
        return results[-1] if results is not None else None

    def evaluate(self, model: Model, split: str = "validation"):
        test_split = self._dataset.splits.get(split)
        x_true = test_split.holdout_matrix.toarray()

        logger.info("Computing predictions")
        x_predict = model.predict(test_split.train_matrix)

        summary_results, user_results, item_results = self.compute_metrics(x_predict, x_true)

        user_ids = list(test_split.user_index.keys())
        user_df = results_to_df(user_results, user_ids)

        item_ids = list(self._dataset.item_index.keys())
        item_df = results_to_df(item_results, item_ids)

        summary_df = pd.DataFrame(summary_results, index=[0])

        model_name = model.name()
        if model_name not in self.evaluated_models:
            self.evaluated_models.append(model_name)
            self._user_results[model_name] = [user_df]
            self._item_results[model_name] = [item_df]
            self._summary_results[model_name] = [summary_df]
        else:
            self._user_results.get(model_name).append(user_df)
            self._item_results.get(model_name).append(item_df)
            self._summary_results.get(model_name).append(summary_df)

    @tmpdir_provider
    def _save_latest_eval(self, model_name: str, checkpoints_dir: str):
        user_results = self._user_results.get(model_name)[-1]
        item_results = self._item_results.get(model_name)[-1]
        summary_results = self._summary_results.get(model_name)[-1]

        write_df(user_results, "user-results.csv")
        write_df(item_results, "item-results.csv")
        write_df(summary_results, "summary-results.csv", index=True)

        write_version(self._version, tmp_dir_path())

        filename = f"model-eval-{model_name}-{current_ts()}.zip"
        file_path = os.path.join(checkpoints_dir, filename)
        zip_dir(file_path, tmp_dir_path())

    def save(self, checkpoints_dir: str) -> None:
        for model in self.evaluated_models:
            self._save_latest_eval(model, checkpoints_dir)

    @tmpdir_provider
    def _load_model_eval(self, model_name: str, zip_path: str):
        unzip_dir(zip_path, tmp_dir_path())

        user_path = os.path.join(tmp_dir_path(), "user-results.csv")
        item_path = os.path.join(tmp_dir_path(), "item-results.csv")
        summary_path = os.path.join(tmp_dir_path(), "summary-results.csv")

        user_results = read_df(user_path, index_col="id")
        item_results = read_df(item_path, index_col="id")
        summary_results = read_df(summary_path)

        self._version = read_version(tmp_dir_path())

        self._user_results[model_name].append(user_results)
        self._item_results[model_name].append(item_results)
        self._summary_results[model_name].append(summary_results)

    def load(self, checkpoints_dir: str, models: List[str], load_prev: bool = True) -> None:
        self.evaluated_models = []

        for model in models:
            pattern = f"model-eval-{model}-*.zip"
            checkpoints = find_checkpoints(checkpoints_dir, pattern, history=(2 if load_prev else 1))

            if checkpoints:
                self._user_results[model] = []
                self._item_results[model] = []
                self._summary_results[model] = []
                self.evaluated_models.append(model)

            for zip_path in reversed(checkpoints):
                self._load_model_eval(model, zip_path)


class DatasetEvaluator:
    def __init__(
        self,
        dataset: Dataset,
        seed: int = 1234,
        verbose: bool = True,
        pymde_neighbors: int = 10,
    ):
        self._dataset = dataset
        self._verbose = verbose
        self._seed = seed
        self._tsne = TSNE(
            n_iter=1500,
            n_components=2,
            metric="cosine",
            init="random",
            verbose=self._verbose,
        )
        self._pca = PCA(n_components=50)
        self.item_embeddings: Optional[DataFrame] = None
        self.user_embeddings: Dict[str, DataFrame] = {}
        self.pymde_neighbors = pymde_neighbors
        self._version: str = CURRENT_VERSION

    def _sample_data(self, X: ndarray, max_samples: int) -> Tuple[ndarray, ndarray]:
        set_seed(self._seed)
        indices = np.random.permutation(X.shape[0])
        indices = indices[:max_samples]
        return X[indices], indices

    def _pymde_embeddings(self, X: Any) -> ndarray:
        pymde.seed(self._seed)
        mde = pymde.preserve_neighbors(X, init="random", n_neighbors=self.pymde_neighbors, verbose=self._verbose)
        embeddings = mde.embed(verbose=self._verbose, max_iter=1000, memory_size=50, eps=1e-6)
        embeddings = embeddings.cpu().numpy()
        return embeddings

    def _tsne_embeddings(self, X: Any) -> ndarray:
        if issparse(X):
            X = X.toarray()
        if X.shape[1] > 50:
            X = self._pca.fit_transform(X)
        embeddings = self._tsne.fit_transform(X)
        return embeddings

    def _compute_embeddings(self, X: csr_matrix, method: str, custom_embeddings: Callable = None):
        if method == "pymde":
            embeds = self._pymde_embeddings(X)
        elif method == "tsne":
            embeds = self._tsne_embeddings(X)
        elif method == "custom" and custom_embeddings is not None:
            embeds = custom_embeddings(X)
            if embeds.shape[1] > 2:
                embeds = self._tsne_embeddings(embeds)
        else:
            raise Exception("Unsupported item embeddings option.")

        return embeds

    def compute_user_embeddings(self, split: str, method: str = "pymde", model: Model = None, max_samples: int = None):
        X = self._dataset.splits.get(split).complete_matrix

        def custom_embeddings(A: csr_matrix):
            return model.compute_embeddings(A)[0]

        embeds = self._compute_embeddings(X, method, custom_embeddings)

        if max_samples is not None:
            embeds, indices = self._sample_data(embeds, max_samples)
        else:
            indices = np.arange(embeds.shape[0])

        ids = np.vectorize(self._dataset.user_index_iterator(split))(indices)
        self.user_embeddings[split] = embeddings_to_df(embeds, ids)

    def compute_item_embeddings(self, method: str = "pymde", model: Model = None):
        X = self._dataset.splits.get("train").complete_matrix.T

        def custom_embeddings(A: csr_matrix):
            return model.compute_embeddings(A.T)[1]

        embeds = self._compute_embeddings(X, method, custom_embeddings)

        indices = np.arange(embeds.shape[0])
        ids = np.vectorize(self._dataset.item_index_to_id)(indices)
        self.item_embeddings = embeddings_to_df(embeds, ids)

    @tmpdir_provider
    def save(self, checkpoints_dir: str) -> None:
        for split, df in self.user_embeddings.items():
            write_df(df, f"user-embeds-{split}.csv")

        if self.item_embeddings is not None:
            write_df(self.item_embeddings, f"item-embeds.csv")

        write_version(self._version, tmp_dir_path())

        filename = f"dataset-eval-{current_ts()}.zip"
        file_path = os.path.join(checkpoints_dir, filename)

        zip_dir(file_path, tmp_dir_path())

    @tmpdir_provider
    def load(self, checkpoints_dir: str) -> None:
        pattern = f"dataset-eval-*.zip"
        checkpoints = find_checkpoints(checkpoints_dir, pattern)

        if checkpoints:
            zip_path = checkpoints[0]
            unzip_dir(zip_path, tmp_dir_path())

            self._version = read_version(tmp_dir_path())

            csv_path = os.path.join(tmp_dir_path(), "item-embeds.csv")
            if os.path.isfile(csv_path):
                self.item_embeddings = read_df(csv_path, index_col="id")

            for split in ["train", "validation"]:
                csv_path = os.path.join(tmp_dir_path(), f"user-embeds-{split}.csv")
                if os.path.isfile(csv_path):
                    self.user_embeddings[split] = read_df(csv_path, index_col="id")
        else:
            raise Exception("No checkpoint to load from.")

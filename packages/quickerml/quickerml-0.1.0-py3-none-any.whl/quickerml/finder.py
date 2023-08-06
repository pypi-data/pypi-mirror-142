import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd
import numpy as np

from colorama import init, deinit, Fore
from tqdm import tqdm
from typing import List
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from pandas.api.types import is_numeric_dtype

from quickerml.exceptions import (
    UnfittableModelError,
    UnsupportedProblemError,
    IncorrectMetricError,
)
from quickerml.metrics import neg_root_mean_squared_error


RANDOM_SEED = 42
ACCEPTED_PROBLEM_TYPES = ("regression", "classification")
DEFAULT_REGRESSORS = [
    XGBRegressor(),
    CatBoostRegressor(verbose=False),
    LGBMRegressor(),
    RandomForestRegressor(random_state=RANDOM_SEED),
]
DEFAULT_REGRESSION_METRICS = [neg_root_mean_squared_error, r2_score]


class Finder:
    def __init__(
        self, problem_type: str, models: List = None, metrics: List = None
    ) -> None:
        if problem_type not in ACCEPTED_PROBLEM_TYPES:
            raise UnsupportedProblemError(
                'Non supported problem type. Try with "regression" or "classification" problems instead.'
            )
        self.problem_type = problem_type

        if metrics is None:
            # Regression problems
            if self.problem_type == ACCEPTED_PROBLEM_TYPES[0]:
                self.metrics = DEFAULT_REGRESSION_METRICS
            # Classification problems
            elif self.problem_type == ACCEPTED_PROBLEM_TYPES[1]:
                # TODO: DEFAULT CLASSIFICATION METRICS
                pass
        else:
            self.metrics = metrics

        if models is None:
            # Regression problems
            if self.problem_type == ACCEPTED_PROBLEM_TYPES[0]:
                self.models = DEFAULT_REGRESSORS
            # Classification problems
            elif self.problem_type == ACCEPTED_PROBLEM_TYPES[1]:
                # TODO: DEFAULT CLASSIFIERS
                pass
        else:
            if not all([hasattr(model, "fit") for model in models]):
                raise UnfittableModelError()
            self.models = models

    def add_model(self, model) -> None:
        self.models.append(model)

    def find(self, X, y, *, return_metrics=False, display=True):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=RANDOM_SEED
        )

        models_performance = pd.DataFrame()
        for model in tqdm(self.models, disable=(not display)):
            model.fit(X_train, y_train)

            results = self._evaluate(model, X_test, y_test)
            models_performance = pd.concat([models_performance, results])

        first_metric = models_performance.iloc[:, 0]
        best_model_idx = np.argmax(first_metric)
        best_model = self.models[best_model_idx]

        if display:
            self._print_performance(models_performance, best_model_idx)

        if return_metrics:
            return best_model, models_performance
        else:
            return best_model

    def _evaluate(self, model, X_test, y_test):
        y_pred = model.predict(X_test)

        try:
            performance = pd.DataFrame(
                {metric.__name__: [metric(y_test, y_pred)] for metric in self.metrics},
                index=[model.__class__.__name__],
            )
        except:
            raise IncorrectMetricError()

        if not all([is_numeric_dtype(performance[column]) for column in performance]):
            raise IncorrectMetricError()

        return performance

    def _print_performance(self, models_performance, colored_row_idx):
        init()
        print()
        for i, row in enumerate(str(models_performance).split("\n")):
            if i == (colored_row_idx + 1):
                print(Fore.GREEN + row + Fore.RESET)
            else:
                print(row)
        print()
        deinit()


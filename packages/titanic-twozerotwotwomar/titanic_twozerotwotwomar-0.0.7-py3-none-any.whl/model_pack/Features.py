import re

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class ReplacingWithNan(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, var=None):
        self.var = None

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X = X.replace("?", np.nan)

        return X


class FeatureDropping(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X.drop(labels=self.variables, axis=1)

        return X


class CovertingToFloat(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        for i in self.variables:
            X[i] = X[i].astype("float")

        return X


class SalutationExtraction(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        def get_title(passenger):
            line = passenger
            if re.search("Mrs", line):
                return "Mrs"
            elif re.search("Mr", line):
                return "Mr"
            elif re.search("Miss", line):
                return "Miss"
            elif re.search("Master", line):
                return "Master"
            else:
                return "Other"

        X["title"] = X[self.variables[0]].apply(get_title)

        return X


class ExtractLetterTransformer(BaseEstimator, TransformerMixin):
    # Extract fist letter of variable

    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError("variables should be a list")

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        for feature in self.variables:
            X[feature] = X[feature].str[0]

        return X


if __name__ == "__main__":
    pass

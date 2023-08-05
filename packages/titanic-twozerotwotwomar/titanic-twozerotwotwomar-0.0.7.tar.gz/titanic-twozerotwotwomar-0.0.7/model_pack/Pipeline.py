#import Features as Fea
import model_pack.Features as Fea
from model_pack.Config.config_validations import _config
from feature_engine.encoding import OneHotEncoder, RareLabelEncoder
from feature_engine.imputation import (
    AddMissingIndicator,
    CategoricalImputer,
    MeanMedianImputer,
)
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# import yaml


# with open('config.yaml','r') as file:
#    y=yaml.safe_load(file)


def titanic_pipe() -> Pipeline:

    # set up the pipeline
    pipeline = Pipeline(
        [
            ("Replacing_?_with_nan", Fea.ReplacingWithNan()),
            (
                "Converting_the_numerical_to_float",
                Fea.CovertingToFloat(variables=_config.pipe_params.NUMERICAL_VARIABLES),
            ),
            (
                "salutation_extraction",
                Fea.SalutationExtraction(variables=_config.pipe_params.SALUTATION),
            ),
            (
                "dropping_features",
                Fea.FeatureDropping(variables=_config.pipe_params.DROP),
            ),
            # ===== IMPUTATION =====
            # impute categorical variables with string 'missing'
            (
                "categorical_imputation",
                CategoricalImputer(variables=_config.pipe_params.CATEGORICAL_VARIABLES),
            ),
            # add missing indicator to numerical variables
            (
                "missing_indicator",
                AddMissingIndicator(variables=_config.pipe_params.NUMERICAL_VARIABLES),
            ),
            # impute numerical variables with the median
            (
                "median_imputation",
                MeanMedianImputer(variables=_config.pipe_params.NUMERICAL_VARIABLES),
            ),
            # Extract first letter from cabin
            (
                "extract_letter",
                Fea.ExtractLetterTransformer(variables=_config.pipe_params.CABIN),
            ),
            # == CATEGORICAL ENCODING ======
            # remove categories present in less than 5% of the observations (0.05)
            # group them in one category called 'Rare'
            (
                "rare_label_encoder",
                RareLabelEncoder(variables=_config.pipe_params.CATEGORICAL_VARIABLES),
            ),
            # encode categorical variables using one hot encoding into k-1 variables
            (
                "categorical_encoder",
                OneHotEncoder(
                    drop_last=True, variables=_config.pipe_params.CATEGORICAL_VARIABLES
                ),
            ),
            # scale using standardization
            ("scaler", StandardScaler()),
            # logistic regression (use C=0.0005 and random_state=0)
            (
                "Logit",
                LogisticRegression(
                    C=_config.model_params.C,
                    random_state=_config.model_params.Model_random_State,
                ),
            ),
        ]
    )

    return pipeline


if __name__ == "__main__":
    # pass
    print(_config.pipe_params.CATEGORICAL_VARIABLES)


# python Pipeline.py

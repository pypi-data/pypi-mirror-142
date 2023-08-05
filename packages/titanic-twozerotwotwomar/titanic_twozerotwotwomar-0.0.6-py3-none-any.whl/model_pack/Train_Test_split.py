import Load_Data  # import data
import pandas as pd
from model_pack.Config.config_validations import _config
from sklearn.model_selection import train_test_split

# import yaml
# with open('config.yaml','r') as file:
#    y = yaml.safe_load(file)


data = Load_Data.data()


def test_train(X: str) -> pd.DataFrame:
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop(_config.split_params.TARGET, axis=1),  # predictors
        data[_config.split_params.TARGET],  # target
        test_size=_config.split_params.test_size,  # percentage of obs in test set
        random_state=_config.split_params.Random_State,
    )  # seed to ensure reproducibility

    if X == "train":
        return X_train, y_train

    if X == "test":
        return X_test, y_test


if __name__ == "__main__":
    print(test_train("train"))
    print(test_train("test"))

# python Train_Test_split.py

from pathlib import Path
from typing import List, Union

from pydantic import BaseModel
from strictyaml import load

cd = Path(__file__).parent
config_file_path = Path.joinpath(cd, "config.yaml")
# config_file_path = Path.joinpath(Path.cwd(),Path('config.yaml'))
# config_file_path = 'config.yaml'


class pipeline_params(BaseModel):
    NUMERICAL_VARIABLES: List[str]
    CATEGORICAL_VARIABLES: List[str]
    CABIN: List[str]
    SALUTATION: List[str]
    DROP: List[str]


class test_train_split_params(BaseModel):
    test_size: float
    Random_State: int
    TARGET: str


class model_params(BaseModel):
    Model_name: str
    C: Union[int, float]
    Model_random_State: int


class config_cummulative(BaseModel):
    pipe_params: pipeline_params
    split_params: test_train_split_params
    model_params: model_params


def config_validate():
    # try:
    with open(config_file_path, "r") as file:
        loaded_config = load(file.read())
    # except Exception as er:
    #    print('Error occured while loading the config file, The error is:')
    #    print(er)

    _config = config_cummulative(
        pipe_params=pipeline_params(**loaded_config.data),
        split_params=test_train_split_params(**loaded_config.data),
        model_params=model_params(**loaded_config.data),
    )

    return _config


_config = config_validate()

#
#
# python Config\config_validations.py
# python Modelling\Config\config_validations.py

if __name__ == "__main__":
    print(config_file_path)
    print(_config.pipe_params)
    # print(Config.model_params)
    # print(cd)

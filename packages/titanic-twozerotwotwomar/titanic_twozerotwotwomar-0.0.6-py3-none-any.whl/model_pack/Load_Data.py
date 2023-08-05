from pathlib import Path

import joblib
import pandas as pd
from model_pack.Config.config_validations import _config
from sklearn.pipeline import Pipeline

cd = Path(__file__).parent
version_file_path = Path.joinpath(cd, "VERSION")

with open(version_file_path) as file:
    ver = file.read()

#path.parent.parent / ('new' + path.suffix)

cd = Path(__file__).parent
data_file_path = Path.joinpath(cd.parent / "Datasets" , "data.csv")
model_file_name = Path(
    "Trained_models/" + _config.model_params.Model_name + "_v" + str(ver) + ".pkl"
)


def data() -> pd.DataFrame:
    data = pd.read_csv(data_file_path)
    for i in data.columns:
        if "." in i:
            i_new = i.replace(".", "_")
            data.rename(columns={i: i_new}, inplace=True)
    return data


def save_model_pipeline(model_pipeline_to_save: Pipeline):
    complete_file_name = Path.joinpath(cd, model_file_name)
    remove_old_model_pipeline()
    joblib.dump(model_pipeline_to_save, complete_file_name)


def load_model_pipeline():
    complete_file_name = Path.joinpath(cd, model_file_name)
    return joblib.load(complete_file_name)


def remove_old_model_pipeline():
    path_name = Path.joinpath(cd, "Trained_models")
    # print(path_name)
    for i in Path(path_name).iterdir():
        # print(i)
        if i != model_file_name:
            i.unlink()
        else:
            raise Exception("File already exists!")


if __name__ == "__main__":
    # print(remove_model_pipeline())
    #print(data().head(5))
    print(model_file_name)
    # pass


# python Production/Modelling/Load_Data.py
# python Load_Data.py

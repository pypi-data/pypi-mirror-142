from model_pack.Load_Data import save_model_pipeline
from model_pack.Pipeline import titanic_pipe
from model_pack.Train_Test_split import test_train


def build_model():
    titanic_pipeline = titanic_pipe()

    X_train, y_train = test_train("train")

    titanic_pipeline.fit(X_train, y_train)

    save_model_pipeline(titanic_pipeline)


build_model()

if __name__ == "__main__":
    pass

# from Pipeline import titanic_pipe
from model_pack.Load_Data import load_model_pipeline
from sklearn.metrics import accuracy_score, roc_auc_score
from model_pack.Train_Test_split import test_train

# python Train_Predict.py


# python Test_Predict.py


def train_val_predictions():

    titanic_pipe = load_model_pipeline()

    X_train, y_train = test_train("train")

    # make predictions for train set
    class_ = titanic_pipe.predict(X_train)
    pred = titanic_pipe.predict_proba(X_train)[:, 1]

    results = dict()

    results["train roc-auc"] = roc_auc_score(y_train, pred)
    results["train accuracy"] = accuracy_score(y_train, class_)

    X_test, y_test = test_train("test")
    class_ = titanic_pipe.predict(X_test)
    pred = titanic_pipe.predict_proba(X_test)[:, 1]

    results["test roc-auc"] = roc_auc_score(y_test, pred)
    results["test accuracy"] = accuracy_score(y_test, class_)

    # determine mse and rmse
    # print('train roc-auc: {}'.format(roc_auc_score(y_train, pred)))
    # print('train accuracy: {}'.format(accuracy_score(y_train, class_)))
    # print()

    # determine mse and rmse
    # print('test roc-auc: {}'.format(roc_auc_score(y_test, pred)))
    # print('test accuracy: {}'.format(accuracy_score(y_test, class_)))
    # print()
    print(results)
    return results


train_val_predictions()

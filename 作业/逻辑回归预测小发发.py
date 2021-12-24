from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def knn_iris_gscv():
    iris = load_iris()
    f = open(r'data1.csv', 'w')
    f.write(iris)
    f.close
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=666)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    y_predict = estimator.predict(x_test)
    report = classification_report(y_test, y_predict, labels=[0, 1, 2], target_names=["类别1", "类别2", "类别3"])
    print(report)


if __name__ == "__main__":
    knn_iris_gscv()

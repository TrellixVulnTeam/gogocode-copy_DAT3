from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.feature_selection import VarianceThreshold
import jieba
import pandas as pd    # 用pandas读取文件

jieba.setLogLevel(jieba.logging.INFO)  # 防止jieba运行时报错


def cut_word(text):
    # 进行中文分词
    return " ".join(list(jieba.cut(text)))  # 不要忘记在""里面加一个空格，意思是用空格分词


def datasets_demo():
    iris = load_iris()  # 获取数据集
    # print(iris)     # 显示数据集
    # print(iris["DESCR"])  # 查看数据集描述
    # print(iris.feature_names)  # 查看特征值的名字
    # print(iris.data)  # 查看特征值
    # print(iris.data.shape)  # 查看样本
    # x_train, x_text, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=66)
    return None


def count_demo():
    # 文本特征抽取
    data = ["life is too short,i like like python",
            "life is too long,i dislike python"]
    # 实例化一个转换器类
    transfer = CountVectorizer()

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())  # .toarray是将其转化为二维数组
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


def count_chinese_demo():
    # 中文文本特征抽取，自动分词
    data = ["你是信的开头诗的内容童话的结尾",
            "你是理所当然的奇迹，你是月色真美",
            "你是圣诞老人送给我好孩子的礼物",
            "你是三千美丽世界里我的一瓢水"]
    data_new = []
    for sent in data:
        data_new.append(cut_word(sent))
    transfer = CountVectorizer(stop_words=["送给"])  # stop_words=[]是指将列表中的内容去除
    data_newer = transfer.fit_transform(data_new)
    print("data_new:\n", data_newer.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


def tfidf_demo():
    # 用TF-IDF的方法进行文本特征抽取
    data = ["所以让我再靠近一点点，因为你太温暖",
            "我会在变得坚强一点点，因为你太柔软",
            "交换无名指金色的契约，给彼此岁月",
            "说好从今以后都牵着手，不管要走多远"]
    data_new = []
    for sent in data:
        data_new.append(cut_word(sent))
    transfer = TfidfVectorizer()
    data_newer = transfer.fit_transform(data_new)
    print("data_new:\n", data_newer.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


def minmax_demo():
    data = pd.read_csv("shuju.txt")
    data = data.iloc[:, :3]
    transfer = MinMaxScaler(feature_range=[0.2])  # 默认[0,1]
    data_new = transfer.fit_transform(data)
    return None


def stand_demo():
    data = pd.read_csv("data.csv")
    data = data.iloc[:, :3]
    print("data:\n", data)
    transfer = StandardScaler()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


def variance_demo():   # variance汉语意思：方差
    # 过滤低方差特征
    data = pd.read_csv("data.csv")
    data = data.iloc[:, 1:-2]
    transfer = VarianceThreshold(threshold=10)   # threshold意思为 阈值
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


if __name__ == "__main__":
    # 代码1：sklearn数据集使用
    # datasets_demo()
    # 代码3：文本特征抽取： CountVecotrizer
    # count_demo()
    # 代码4：中文文本特征抽取，自动分词：
    # count_chinese_demo()
    # tfidf_demo()
    # minmax_demo()
    # stand_demo()
    variance_demo()

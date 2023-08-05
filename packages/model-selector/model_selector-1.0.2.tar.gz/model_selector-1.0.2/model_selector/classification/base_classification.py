import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def fix_missing_data(dataset):
    """
    This function receives a dataset as input, fixes missing data by finding the mean of the columns with missing
    data and replacing the missing data with the calculated means.
    :param dataset: csv data
    :return: dataset with no missing data
    """
    inputter = SimpleImputer(missing_values=np.nan, strategy='mean')
    inputter.fit(dataset[:])
    dataset[:] = inputter.transform(dataset[:])
    return dataset


class Base:
    """
    This class contains all methods that are common to all defined classification models
    """

    def __init__(self, file_path):
        self.classifier = None
        self.file_path = file_path
        self.x = []
        self.y = []
        self.x_train = []
        self.x_test = []
        self.y_train = []
        self.y_test = []
        self.y_pred = []

    def import_dataset(self):
        """
        This function reads the dataset and assigns, fixes missing data  and splits data into x and y
        :return: self
        """
        dataset = pd.read_csv(self.file_path)
        dataset_fixed = fix_missing_data(dataset)
        self.x = dataset_fixed.iloc[:, :-1].values
        self.y = dataset_fixed.iloc[:, -1].values
        return self

    def split_dataset(self, test_size=0.2):
        """
        This function splits the dataset into train and test
        :param test_size: splitting data test size. (optional)
        :return: self
        """
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=test_size,
                                                                                random_state=0)
        return self

    def feature_scale(self):
        """
        This function does feature scaling of the train and test datasets.
        :return: self
        """
        sc = StandardScaler()
        self.x_train = sc.fit_transform(self.x_train)
        self.x_test = sc.transform(self.x_test)
        return self

    def train_model(self):
        """
        This method fits the regression model
        :return: self
        """
        self.classifier.fit(self.x_train, self.y_train)

    def confusion_matrix(self, model_name):
        """
        This function creates the confusion matrix with the test and predicted y values
        :param model_name: classification model name
        :return: classification metrics with accurate score
        """
        self.y_pred = self.classifier.predict(self.x_test)
        metrics = {"Model Name": f"{model_name}",
                   # "Precision Score": precision_score(self.y_test, self.y_pred, average=None, zero_division=1),
                   # "Recall Score": recall_score(self.y_test, self.y_pred, average=None, zero_division=1),
                   "Accuracy Score": accuracy_score(self.y_test, self.y_pred),
                   }
        return metrics

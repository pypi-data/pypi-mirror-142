import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split


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
    This class contains all methods that are common to all defined regression models
    """
    def __init__(self, file_path):
        self.regressor = None
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

    def train_model(self):
        """
        This method fits the regression model
        :return: regressor
        """
        self.regressor.fit(self.x_train, self.y_train)

    def predict_test(self):
        """
        This function runs the regressor predictions
        :return: y_pred
        """
        self.y_pred = self.regressor.predict(self.x_test)

    def evaluate_metrics(self, model_name):
        """
        This function returns the key metrics for the regression
        :param model_name: regression model name
        :return: regression metrics with r2 score
        """
        metrics = {"Model Name": f"{model_name}",
                   "Mean Squared Error": mean_squared_error(self.y_test, self.y_pred),
                   "Mean Absolute Error": mean_absolute_error(self.y_test, self.y_pred),
                   "R2 Score": round(r2_score(self.y_test, self.y_pred), 4),
                   }
        return metrics

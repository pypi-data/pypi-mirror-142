from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from model_selector.regression.base_regression import Base


class MultipleLinear(Base):
    """
    This class performs a multiple linear regression. It inherits from the Base class from the base_regression.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.regressor = LinearRegression()

    def __str__(self):
        """
        :return: The name of the class
        """
        return "Multiple Linear"


class DecisionTree(Base):
    """
    This class performs a decision tree regression. It inherits from the Base class from the base_regression.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.regressor = DecisionTreeRegressor(random_state=0)

    def __str__(self):
        """
        :return: The name of the class
        """
        return "Decision Tree"


class Polynomial(Base):
    """
    This class performs a polynomial regression. It inherits from the Base class from the base_regression.py module
    """

    def __init__(self, file_path, polynomial_degree=4):
        super().__init__(file_path)
        self.file_path = file_path
        self.regressor = LinearRegression()
        self.poly_reg = PolynomialFeatures(degree=polynomial_degree)

    def train_model(self):
        """
       This method fits the regression model
       :return: regressor
       """
        x_poly = self.poly_reg.fit_transform(self.x_train)
        self.regressor.fit(x_poly, self.y_train)

    def predict_test(self):
        """
        This function runs the regressor predictions
        :return: y_pred
        """
        self.y_pred = self.regressor.predict(self.poly_reg.transform(self.x_test))

    def __str__(self):
        """
        :return: The name of the class
        """
        return "Polynomial"


class RandomForest(Base):
    """
    This class performs a random forest regression. It inherits from the Base class from the base_regression.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.regressor = RandomForestRegressor(n_estimators=10, random_state=0)

    def __str__(self):
        """
        :return: The name of the class
        """
        return "Random Forest"


class SupportVector:
    pass

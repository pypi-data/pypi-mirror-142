from model_selector.classification.base_classification import Base
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


class LogisticReg(Base):
    """
    This class performs a logistic regression. It inherits from the Base class from the base_classification.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = LogisticRegression(random_state=0)

    def __str__(self):
        return "Logistic Regression"


class DecisionTree(Base):
    """
    This class performs a decision tree classification. It inherits from the Base class from the
    base_classification.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

    def __str__(self):
        return "Decision Tree"


class KNearestNeighbors(Base):
    """
    This class performs a K Nearest Neighbors classification. It inherits from the Base class from the
    base_classification.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)

    def __str__(self):
        return "K-Nearest Neighbors"


class KernelSVM(Base):
    """
    This class performs a Kernel SVM classification. It inherits from the Base class from the base_classification.py
    module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = SVC(kernel='rbf', random_state=0)

    def __str__(self):
        return "Kernel SVM"


class NaiveBayes(Base):
    """
    This class performs a Naive Bayes classification. It inherits from the Base class from the base_classification.py
    module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = GaussianNB()

    def __str__(self):
        return "Naive Bayes"


class RandomForest(Base):
    """
    This class performs a Random Forest classification. It inherits from the Base class from the
    base_classification.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)

    def __str__(self):
        return "Random Forest"


class SupportVectorMachine(Base):
    """
    This class performs a support vector machine classification. It inherits from the Base class from the
    base_classification.py module
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.classifier = SVC(kernel='linear', random_state=0)

    def __str__(self):
        return "Support Vector Machine"

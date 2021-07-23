from log.logger import Logger
from preprocessing.preprocess import Preprocess
from constants.config import Constants
import pickle


class Test(object):

    def __init__(self):
        self.log_save_file_name = 'Test'
        self.logger_obj = Logger(self.log_save_file_name)
        self.ps = Preprocess()
        self.model = None

    def load_model(self):
        try:
            with open(f"{Constants.MODELS_MUSICAL}/RandomForest.pickle", 'rb') as pickle_file:
                self.model = pickle.load(pickle_file)
        except Exception as ex:
            self.logger_obj.error(ex, "Test class, load_model")

    def predict(self, predict_data):
        try:
            self.load_model()
            return self.model.predict(predict_data)
        except Exception as ex:
            self.logger_obj.error(ex, "Test class, predict")



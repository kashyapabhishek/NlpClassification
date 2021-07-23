from constants.config import Constants
from log.logger import Logger
import os
import pandas as pd


class Datasets(object):

    def __init__(self):
        self.musical_dataset_path = os.path.join(os.getcwd(), Constants.DATA_MUSICAL)
        self.dataset = None
        self.log_save_file_name = 'LoadDatasets'
        self.logger_obj = Logger(self.log_save_file_name)

    def musical_instruments_reviews(self):
        try:
            self.logger_obj.info("dataset load start")
            self.dataset = pd.read_csv(self.musical_dataset_path)
            self.logger_obj.info("dataset load end")
            return self.dataset
        except Exception as ex:
            self.logger_obj.error(ex, "Datasets class, musical_instruments_reviews")


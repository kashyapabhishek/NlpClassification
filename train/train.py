from log.logger import Logger
from preprocessing.preprocess import Preprocess


class Train(object):
    def __init__(self):
        self.log_save_file_name = 'Train'
        self.logger_obj = Logger(self.log_save_file_name)
        self.ps = Preprocess()

    def start(self):
        try:
            self.logger_obj.info('fill_null_valued start')
            self.ps.fill_null_valued()

            self.logger_obj.info('create_clean_feature start')
            self.ps.create_clean_feature()

            self.logger_obj.info('select_clean_data start')
            self.ps.select_clean_data()

            self.logger_obj.info('remove_extra_word_tokenize_and_lemmatize start')
            self.ps.remove_extra_word_tokenize_and_lemmatize()

            self.logger_obj.info('vectorizer start')
            self.ps.vactorizer()

            self.logger_obj.info('train_test_split start')
            self.ps.train_test_split()

            self.logger_obj.info('create_pipeline start')
            self.ps.create_pipeline()

            self.logger_obj.info('create_model start')
            self.ps.create_model()
            self.logger_obj.info('model created')
        except Exception as ex:
            self.logger_obj.error(ex, "Train class, start")

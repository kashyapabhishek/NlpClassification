from log.logger import Logger
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from constants.config import Constants
import numpy as np
from load_datasets.datasets import Datasets
import pickle
import re
import os


class Preprocess(object):

    def __init__(self):
        self.data = Datasets().musical_instruments_reviews()
        self.log_save_file_name = 'Preprocess'
        self.logger_obj = Logger(self.log_save_file_name)
        self.data_clean = None
        self.words = stopwords.words("english")
        self.lemmatizer = WordNetLemmatizer()
        self.vectorizer = None
        self.final_features = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.pipeline = None
        self.ytest = None

    def fill_null_valued(self):
        try:
            self.data = self.data.fillna('other')
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, fill_null_valued")

    def create_clean_feature(self):
        try:
            summery = []
            for d in range(self.data.shape[0]):
                text = ''
                for i in range(3):
                    text += ' ' + self.data.iloc[d][i]
                summery.append(text)
            self.data['clean'] = summery
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, create_clean_feature")

    def select_clean_data(self):
        try:
            self.data_clean = self.data[['clean', 'overall']]
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, select_clean_data")

    def remove_extra_word_tokenize_and_lemmatize(self):
        try:
            self.data_clean['clean'] = self.data_clean['clean'].apply(lambda x: re.sub(r'[^\w\s]', '', x.lower()))
            self.data_clean['clean'] = self.data_clean['clean'].apply(lambda x: word_tokenize(x))
            self.data_clean['clean'] = self.data_clean['clean'].apply(lambda x: [i for i in x if x not in self.words])
            self.data_clean['clean'] = self.data_clean['clean'].apply(lambda x: list(map(self.lemmatizer.lemmatize, x)))
            self.data_clean['clean'] = self.data_clean['clean'].apply(lambda x: ' '.join(x))
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, remove_extra_word_tokenize_and_lemmatize")

    def vactorizer(self):
        try:
            self.vectorizer = TfidfVectorizer(min_df=3, stop_words="english", sublinear_tf=True, norm='l2', ngram_range=(1, 2))
            self.final_features = self.vectorizer.fit_transform(self.data_clean['clean']).toarray()
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, vactorizer")

    def train_test_split(self):
        try:
            X = self.data_clean['clean']
            y = self.data_clean['overall']
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.25)
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, train_test_split")

    def create_pipeline(self):
        try:
            self.pipeline = Pipeline([('vect', self.vectorizer),
                                 ('chi', SelectKBest(chi2, k=1200)),
                                 ('clf', RandomForestClassifier())])
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, create_pipeline")

    def create_model(self):
        try:
            model = self.pipeline.fit(self.X_train, self.y_train)
            if not os.path.isdir(f"{Constants.MODELS_MUSICAL}"):
                os.mkdir(f"{Constants.MODELS_MUSICAL}")
            if os.path.isfile(f'{Constants.MODELS_MUSICAL}/RandomForest.pickle'):
                os.rename(f'{Constants.MODELS_MUSICAL}/RandomForest.pickle', f'{Constants.MODELS_MUSICAL}/RandomForestBackup.pickle')
            with open(f'{Constants.MODELS_MUSICAL}/RandomForest.pickle', 'wb') as f:
                pickle.dump(model, f)
            self.ytest = np.array(self.y_test)
        except Exception as ex:
            self.logger_obj.error(ex, "Preprocess class, create_model")















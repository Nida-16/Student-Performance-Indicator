import os
import sys
import numpy as np
import pandas as pd
from src.utils import save_object
from src.logger import logging
from src.exception import CustomExceptionHandling
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join(r'artifacts', r'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            categorical_cols = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]
            numerical_cols = ['reading_score',
                              'writing_score']

            cat_pipeline = Pipeline(
                steps=[("imputer", SimpleImputer(strategy='most_frequent')),
                       ("one_hot_encoder", OneHotEncoder()),
                       ("scaler", StandardScaler(with_mean=False))])
            # logging.info("---> Categorical columns One Hot Encoded --->")
            logging.info(f"Categorical columns : {categorical_cols}")

            num_pipeline = Pipeline(
                steps=[("imputer", SimpleImputer(strategy='median')),
                       ("scaler", StandardScaler(with_mean=False))])
            # logging.info("---> Numerical columns Standard Scaled --->")
            logging.info(f"Numerical columns : {numerical_cols}")

            preprocessor = ColumnTransformer(
                [("cat_pipeline", cat_pipeline, categorical_cols),
                 ("num_pipeline", num_pipeline, numerical_cols)])

            return preprocessor

        except Exception as e:
            raise CustomExceptionHandling(e, sys)

    # We wil get train_path & test_path from data_ingestion
    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Reading of Train & Test data completed")

            logging.info("Obtaining preprocessor object ...")
            preprocessor_obj = self.get_data_transformer_object()

            target_col = 'math_score'

            input_features_train_df = train_df.drop([target_col], axis=1)
            target_features_train_df = train_df[target_col]

            input_features_test_df = test_df.drop([target_col], axis=1)
            target_features_test_df = test_df[target_col]

            logging.info(
                "Applying preprocessor object on training and testing df")

            input_features_train_arr = preprocessor_obj.fit_transform(
                input_features_train_df)
            input_features_test_arr = preprocessor_obj.transform(
                input_features_test_df)

            train_arr = np.c_[input_features_train_arr,
                              np.array(target_features_train_df)]

            test_arr = np.c_[input_features_test_arr,
                             np.array(target_features_test_df)]
            logging.info(
                self.data_transformation_config.preprocessor_file_path)
            save_object(
                file_path=self.data_transformation_config.preprocessor_file_path,
                obj=preprocessor_obj
            )

            logging.info("Preprocessor object saved")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_file_path
            )

        except Exception as e:
            raise CustomExceptionHandling(e, sys)

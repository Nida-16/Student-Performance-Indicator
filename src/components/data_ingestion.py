import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomExceptionHandling
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# when only variables need to be defined use @dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('artifacts', 'test_data.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw_data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Logged into data ingestion component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info("---> Dataset read as DataFrame --->")

            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)

            logging.info("---> Train test split initiated --->")
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,
                             index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)
            logging.info("---> Data ingestion completed --->")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomExceptionHandling(e, sys)


if __name__ == "__main__":
    di_obj = DataIngestion()
    train_data, test_data = di_obj.initiate_data_ingestion()

    dt = DataTransformation()
    train_data, test_data, preprocessor_obj_file_path = dt.initiate_data_transformation(
        train_data, test_data)

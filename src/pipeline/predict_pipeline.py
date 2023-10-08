import sys
import pandas as pd
from src.exception import CustomExceptionHandling
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model_path = 'artifacts\model.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            model = load_object(file_path=model_path)

            scaled_data = preprocessor.transform(features)
            preds = model.predict(scaled_data)
            return preds
        
        except Exception as e:
            raise CustomExceptionHandling(e, sys)


class CustomData:
    def __init__(self,
                 gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_As_dataframe(self):
        try:
            input_dictionary = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }

            return pd.DataFrame(input_dictionary)

        except Exception as e:
            raise CustomExceptionHandling(e, sys)

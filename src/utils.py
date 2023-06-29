import os
import sys
import dill
from src.exception import CustomExceptionHandling


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        print("--------------", dir_path)
        with open(dir_path, 'wb') as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomExceptionHandling(e, sys)

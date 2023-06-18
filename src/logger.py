import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"  # name of specific log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)           # generally appending any log file
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)        # path of that specific log file

logging.basicConfig(filename=LOG_FILE_PATH, 
                    format = "[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

# if __name__=="__main__":
#     logging.info("Logging has started")





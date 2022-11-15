import os
import sys
import logging

##logging configuration
logging_string= "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir= "logs"
log_filepath= os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format= logging_string,
    handlers=[
        logging.StreamHandler(sys.stdout),## Generare run time message
        logging.FileHandler(log_filepath),##print in the file
    ]
)
logger= logging.getLogger("deepClassifierLogger")
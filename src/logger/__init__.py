import logging
import os
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime

# # If you have from_root, use it; else fallback to os.getcwd()
# try:
#     from from_root import from_root
# except ImportError:
#     from_root = lambda: os.getcwd()

# Constant for log configuration
LOG_DIR  = "logs"
LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
MAX_LOG_SIZE = 5*1024*1024 #5 mB
BACKUP_COUNT  = 3 #Number of the backup log files to keep

# Construct log file path
log_dir_path = os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path = os.path.join(log_dir_path,LOG_FILE)

def configure_logger():
    logger = logging.getLogger()
    logger.setLevel('DEBUG')

    #DEFINE FORMATTER
    formatter = logging.Formatter("[%(asctime)s] %(name)s - %(levelname)s - %(message)s")

    # FILE HANDLER WITH ROTATOR
    file_handler = RotatingFileHandler(log_file_path , maxBytes=MAX_LOG_SIZE ,backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # CONSOLE HANDLER
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    #Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# CONFIGURE THE LOGGER
configure_logger()






 

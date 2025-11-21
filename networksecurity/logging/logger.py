import os
import logging
from datetime import datetime
log_path=f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
log_file=os.path.join(os.getcwd(),"logs",log_path)
os.makedirs(log_file,exist_ok=True)
log_file_path=os.path.join(log_file,log_path)
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO
)
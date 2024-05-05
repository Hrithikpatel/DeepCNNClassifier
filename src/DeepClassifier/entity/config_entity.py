import sys
from collections import namedtuple
from DeepClassifier.constant import PROJECT_ROOT_DIR
sys.path.append(PROJECT_ROOT_DIR)



DataIngestionConfig = namedtuple("DataIngestionConfig",[
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir"
])


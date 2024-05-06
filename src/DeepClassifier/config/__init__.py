import sys
import os
from DeepClassifier.constant import CONFIG_FILE_PATH,PARAMS_FILE_PATH,PROJECT_ROOT_DIR
from DeepClassifier.utils import *
from DeepClassifier.entity import DataIngestionConfig
sys.path.append(PROJECT_ROOT_DIR)

class ConfigurationManager:

    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    

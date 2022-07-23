from os import environ as env, path, mkdir
import json
import logging
import numpy as np
import pandas as pd
from environment.constants import EnvironmentVariables

# def configure_environment_from_file(file_path = './appsettings.json'):
#     if(path.exists(file_path)):
#         logging.info('Configurating environment from file...\n')
#         with open(file_path) as file:
#             configurations = json.load(file)
#             env["VAR"] = configurations["VAR"]

def configurate_logging():
    logging.basicConfig(format="%(asctime)s: %(message)s",
                        level=logging.INFO, 
                        datefmt="%H:%M:%S")   
    logging.info('Logging configurated')

def configure_pandas():
    pd.set_option('mode.chained_assignment', None)

def configure_numpy_seed():
    np.random.seed(EnvironmentVariables.SEED)

def prepare_environment():
    configurate_logging()    
    configure_pandas()
    configure_numpy_seed()
    # configure_environment_from_file() 
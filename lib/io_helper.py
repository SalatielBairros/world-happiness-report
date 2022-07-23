from os.path import exists
from os import mkdir

def create_directory_if_not_exists(path):
    if not exists(path):
        mkdir(path)
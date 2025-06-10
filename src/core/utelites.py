import base64
import json
import os
import random
import time

from src.core.settings import BASE_DIR, base_folder_name


##### FOLDER ####
def create_basic_folders():
    "Создает папки необходимык для работы. Изменить или доваить в base_folder_name"
    dir_root = os.listdir(BASE_DIR)
    for name in base_folder_name:
        if name not in dir_root:
            path = os.path.join(BASE_DIR, name)
            os.mkdir(path)


def not_big_sleep():
    """Спит для дереходов между объектами """
    time.sleep(random.random() * 77 / 27.9)


def big_sleep():
    """Спит для ожидания загрузки меток на карте """
    time.sleep(random.random() * 77 / 13.9)


if __name__ == '__main__':
    ...

import os.path
from pathlib import Path

# Постройте пути внутри проекта следующим образом.: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
base_folder_name = ['logs', 'static', 'download', 'export_csv']
STATIC_DIR = os.path.join(BASE_DIR, 'static')
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'download')
EXPORT_DIR = os.path.join(BASE_DIR, 'export_csv')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
# Создадим папки

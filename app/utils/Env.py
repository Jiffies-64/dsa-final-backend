import os
from dotenv import load_dotenv

load_dotenv()

# 数据库相关
DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
DB_PORT = os.environ.get('DB_PORT')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

# 发送邮件相关
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
SENDER_PASSWD = os.environ.get('SENDER_PASSWD')

# 与模型相关
OFFLOAD_FOLDER = os.environ.get('OFFLOAD_FOLDER')

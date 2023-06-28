import logging
import time
from logging import handlers
import os

base_path = os.path.dirname(os.path.abspath(__file__))
base_url = 'https://testapp.xmnewyea.com/app_manage'
app_version = '1.1'
app_type = '2'
device_id = '666666'
db_user = 'root'
db_password = 'ny123456'
db_localhost = '120.78.20.142'
db_database = 'test_new_yea_app'
db_port = '3308'


# 初始化日志配置
def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建控制台处理器
    sh = logging.StreamHandler()
    # 创建文件处理器
    log_file = base_path+'/log/log_{}.log'.format(time.strftime("%Y-%m-%d %H-%M-%S"))
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='M', interval=1, backupCount=3)

    # 创建格式化器
    fms = "%(levelname)s %(filename)s %(lineno)d %(asctime)s %(message)s"
    fm = logging.Formatter(fmt=fms)

    # 将格式化器添加到处理器中
    fh.setFormatter(fm)
    sh.setFormatter(fm)

    # 将处理器添加到日志器中
    logger.addHandler(fh)
    logger.addHandler(sh)






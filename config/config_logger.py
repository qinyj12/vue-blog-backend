import logging

# 日志系统配置
def initialize_logger():
    handler = logging.FileHandler('logs/app.log', encoding='UTF-8')
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)

    return handler
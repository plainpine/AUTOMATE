import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.critical('致命的エラー! 致命的エラー!')
logging.disable(logging.CRITICAL)
logging.critical('致命的エラー! 致命的エラー!')
logging.error('エラー! エラー!')

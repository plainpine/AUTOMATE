import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('デバッグ用詳細情報')
logging.info('loggingモジュールは動作中')
logging.warning('エラーメッセージがログ出力されようとしている')
logging.error('エラーが発生した')
logging.critical('プログラムは回復不能!')

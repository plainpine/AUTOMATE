import traceback, os
from pathlib import Path
os.chdir(Path.home())
try:
    raise Exception('これはエラーメッセージです。')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('トレースバック情報をerrorInfo.txtに書きました')

import os
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print(f'現在のディレクトリは ' + folderName)
    for subfolder in subfolders:
        print(f'{folderName} のサブディレクトリ: {subfolder}')
    for filename in filenames:
        print(f'{folderName}内 のファイル: {filename}')
    print('')

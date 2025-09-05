# convertSpreadsheet.py
# Usage commandline: pyhton convertSpreadsheet.py <file.name>

import ezsheets,sys

spreadsheetOld=sys.argv[1]
ss=ezsheets.upload(spreadsheetOld)
print('Spreadsheet name: '+ ss.title)
ss.downloadAsCSV()
print('Done!')

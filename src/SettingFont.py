import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb['Sheet']
italic24Font = Font(size=24, italic=True) # フォント作成　❶
sheet['A1'].font = italic24Font # A1にフォントを設定 ❷
sheet['A1'] = 'Hello, world!'
wb.save('styles.xlsx')

import openpyxl
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2' # A2より上の行を固定
wb.save('freezeExample.xlsx')

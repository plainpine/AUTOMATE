import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
list(sheet.columns)[1] # 第２列を取得
print(list(sheet.columns)[1])

for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)

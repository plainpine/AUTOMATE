import ezsheets
ss = ezsheets.upload('produceSales3.xlsx')
sheet = ss.sheets[0]
sheet.getRow(1)  # The first row is row 1, not row 0.
print(sheet.getRow(1))

sheet.getRow(2)
print(sheet.getRow(2))

sheet.getColumn(1)
print(sheet.getColumn(1))

sheet.getColumn('A')  # The same result as getColumn(1)
print(sheet.getColumn('A') )

sheet.getRow(3)
print(sheet.getRow(3))

sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
sheet.getRow(3)
print(sheet.getRow(3))

columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    # Make the Python list contain uppercase strings:
    columnOne[i] = value.upper()

sheet.updateColumn(1, columnOne)  # Update the entire column in one request.

rows = sheet.getRows()  # Get every row in the spreadsheet.
rows[0]  # Examine the values in the first row.
print(rows[0])

rows[1]
print(rows[1])

rows[1][0] = 'PUMPKIN'  # Change the produce name.
rows[1]
print(rows[1])

rows[10]
print(rows[10])

rows[10][2] = '400'  # Change the pounds sold.
rows[10][3] = '904'  # Change the total.
rows[10]
print(rows[10])

sheet.updateRows(rows)  # Update the online spreadsheet with the changes.
sheet.rowCount  # The number of rows in the sheet
print(sheet.rowCount)

sheet.columnCount  # The number of columns in the sheet
print(sheet.columnCount)

sheet.rowCount=16
sheet.rowCount
print(sheet.rowCount)

sheet.columnCount = 4  # Change the number of columns to 4.
sheet.columnCount  # Now the number of columns in the sheet is 4.print(sheet.columnCount)
print(sheet.columnCount)

import ezsheets
ss = ezsheets.Spreadsheet()  # Starts with a sheet named Sheet1
sheet2 = ss.Sheet('Spam')
sheet3 = ss.Sheet('Eggs')
ss.sheets  # The Sheet objects in this Spreadsheet, in order
print(ss.sheets)

ss.sheetTitles  # The titles of all the Sheet objects in this Spreadsheet
print(ss.sheetTitles)

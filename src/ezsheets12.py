import ezsheets
ss = ezsheets.Spreadsheet()
ss.title = 'Multiple Sheets'
ss.sheetTitles
print(ss.sheetTitles)

sheetname = ss.createSheet('Spam')  # Create a new sheet at the end of the list of sheets.
print(sheetname)

sheetname = ss.createSheet('Eggs')  # Create another new sheet.
print(sheetname)

ss.sheetTitles
print(ss.sheetTitles)

sheetname = ss.createSheet('Bacon', 0)  # Create a sheet at index 0 in the list of sheets.
print(sheetname)

ss.sheetTitles
print(ss.sheetTitles)

ss.sheets[0].index
ss.sheetTitles
print(ss.sheets[0].index)

ss.sheets[0].index = 2  # Move the sheet at index 0 to index 2.
ss.sheetTitles
print(ss.sheetTitles)

ss.sheets[2].index = 0  # Move the sheet at index 2 to index 0.
ss.sheetTitles
print(ss.sheetTitles)

ss.sheets[0].delete()  # Delete the sheet at index 0: the "Bacon" sheet.
ss.sheetTitles
print(ss.sheetTitles)

ss['Spam'].delete()  # Delete the "Spam" sheet.
ss.sheetTitles
print(ss.sheetTitles)

sheet = ss['Eggs']  # Assign a variable to the "Eggs" sheet.
sheet.delete()  # Delete the "Eggs" sheet.
ss.sheetTitles
print(ss.sheetTitles)

ss.sheets[0].clear()  # Clear all the cells on the "Sheet1" sheet.
ss.sheetTitles  # The "Sheet1" sheet is empty but still exists.
print(ss.sheetTitles)

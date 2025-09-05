import ezsheets
ss1 = ezsheets.Spreadsheet()
ss1.title = 'First Spreadsheet'
ss1.sheets[0].title = 'Spam'  # ss1 will have a sheet named Spam.
ss2 = ezsheets.Spreadsheet()
ss2.title = 'Second Spreadsheet'
ss2.sheets[0].title = 'Eggs'  # ss2 will have a sheet named Eggs.
ss1[0]
print(ss1[0])

ss1[0].updateRow(1, ['Some', 'data', 'in', 'the', 'first', 'row'])
ss1[0] .copyTo(ss2)  # Copy the ss1's Sheet1 to the ss2 spreadsheet.
ss2.sheetTitles  # ss2 now contains a copy of ss1's Sheet1.
print(ss2.sheetTitles)

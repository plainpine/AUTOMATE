import ezsheets
ss = ezsheets.Spreadsheet()
ss.title = 'My Spreadsheet'
sheet = ss.sheets[0]  # Get the first sheet in this spreadsheet.
sheet.title
print(sheet.title)

sheet['A1'] = 'Name'  # Set the value in cell A1.
sheet['B1'] = 'Age'
sheet['C1'] = 'Favorite Movie'
sheet['A1']  # Read the value in cell A1.
print(sheet['A1'])

sheet['A2']  # Empty cells return a blank string.
print(sheet['A2'])

sheet[2, 1]  # Column 2, Row 1 is the same address as B1.
print(sheet[2, 1])

sheet['A2'] = 'Alice'
sheet['B2'] = 30
sheet['C2'] = 'RoboCop'
sheet['B2']  # Note that all data is returned as strings.
print(sheet['B2'])

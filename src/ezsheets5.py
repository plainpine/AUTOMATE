import ezsheets
example_ss = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1OAoid-o7MDr-Mg8b-JeziYbEN1zTqzTopKBpuEuPX-A/')
ss = ezsheets.Spreadsheet()
example_ss.sheets[0].copyTo(ss)
ss.sheets[0].delete()  # Delete the Sheet1 sheet.
ss.url
print(ss.url)

ss.title  # The title of the spreadsheet
print(ss.title)

ss.title = 'Sweigart Books'  # Change the title.
ss.id  # The unique ID (a read-only attribute)
print(ss.id)

ss.url  # The original URL (a read-only attribute)
print(ss.url)

ss.sheetTitles  # The titles of all the Sheet objects
print(ss.sheetTitles)

ss.sheets  # The Sheet objects in this Spreadsheet, in order
print(ss.sheets)

ss.sheets[0]  # The first Sheet object in this Spreadsheet
print(ss.sheets[0])

ss['シート1 のコピー']  # Sheets can also be accessed by title.
print(ss['Copy of Books'])

ss.Sheet('New blank sheet')  # Create a new sheet.
print(ss.Sheet('New blank sheet'))

ss.sheets[1].delete()  # Delete the second Sheet object in this Spreadsheet.

ss.refresh()

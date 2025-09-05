import ezsheets
ss = ezsheets.createSpreadsheet('Delete me')  # Create the spreadsheet.
ezsheets.listSpreadsheets()  # Confirm that we've created a spreadsheet.
print(ezsheets.listSpreadsheets())

ss.delete()  # Delete the spreadsheet.
ezsheets.listSpreadsheets()  # Spreadsheets in the Trash folder are still listed.
print(ezsheets.listSpreadsheets())

ss.delete(permanent=True)
ezsheets.listSpreadsheets()
print(ezsheets.listSpreadsheets())

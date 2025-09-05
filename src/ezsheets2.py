import ezsheets
ss2 = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1OAoid-o7MDr-Mg8b-JeziYbEN1zTqzTopKBpuEuPX-A/')
ss3 = ezsheets.Spreadsheet('1OAoid-o7MDr-Mg8b-JeziYbEN1zTqzTopKBpuEuPX-A')
ss2 == ss3  # These are the same spreadsheet.
print(ss2 == ss3)

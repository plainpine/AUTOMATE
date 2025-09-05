import ezsheets
ezsheets.convertAddress('A2')  # Converts addresses...
print(ezsheets.convertAddress('A2'))

ezsheets.convertAddress(1, 2)  # ...and converts them back, too.
print(ezsheets.convertAddress(1, 2))

ezsheets.getColumnLetterOf(2)
print(ezsheets.getColumnLetterOf(2))

ezsheets.getColumnNumberOf('B')
print(ezsheets.getColumnNumberOf('B'))

ezsheets.getColumnLetterOf(999)
print(ezsheets.getColumnLetterOf(999))

ezsheets.getColumnNumberOf('ZZZ')
print(ezsheets.getColumnNumberOf('ZZZ'))

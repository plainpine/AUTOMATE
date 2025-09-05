import ezsheets

# Replace this with your actual spreadsheet ID
SPREADSHEET_ID = '1KA24I13wl-4dkYg5f4vI792A3y3iIzS52Q3v5VmdoCo'

# Load the spreadsheet
ss = ezsheets.Spreadsheet(SPREADSHEET_ID)

# Assume responses are on the first sheet
sheet = ss[0]

# Get all rows (as a list of lists)
rows = sheet.getRows()

# Print the header to determine the index of the 'Email Address' column
print('Headers:', rows[0])

# Assume first row is header, skip it
email_index = rows[0].index('Email')

# Extract emails from each row
emails = [row[email_index] for row in rows[1:] if row[email_index]]

print('\nCollected Email Addresses:')
for email in emails:
    print(email)

filename = ss.downloadAsExcel()
print(filename)

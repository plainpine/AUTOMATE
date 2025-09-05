import ezsheets
ss = ezsheets.Spreadsheet('1OAoid-o7MDr-Mg8b-JeziYbEN1zTqzTopKBpuEuPX-A')
ss.title
print(ss.title)

filename = ss.downloadAsExcel()  # Downloads the spreadsheet as an Excel file
print(filename)

filename = ss.downloadAsODS()  # Downloads the spreadsheet as an OpenOffice file
print(filename)

filename = ss.downloadAsCSV()  # Downloads only the first sheet as a CSV file
print(filename)

filename = ss.downloadAsTSV()  # Downloads only the first sheet as a TSV file
print(filename)

filename = ss.downloadAsPDF()  # Downloads the spreadsheet as a PDF
print(filename)

filename = ss.downloadAsHTML()  # Downloads the spreadsheet as a ZIP of HTML files
print(filename)

filename = ss.downloadAsExcel('a_different_filename.xlsx')
print(filename)

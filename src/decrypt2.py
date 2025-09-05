import pypdf

# PDFファイルの読み込み
pdfReader = pypdf.PdfReader('encrypted.pdf')
pdfReader.decrypt('rosebud')

pageObj = pdfReader.pages[0]
print(pageObj)

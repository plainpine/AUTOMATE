import pypdf

# PDFファイルの読み込み
pdfReader = pypdf.PdfReader('encrypted.pdf')
pdfReader.is_encrypted
print(pdfReader.is_encrypted)

pdfReader.pages[0]

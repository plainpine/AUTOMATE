import pypdf

## PDFファイルの読み込み
pdfReader = pypdf.PdfReader('meetingminutes.pdf')

# ページ数の取得
number_of_pages = len(pdfReader.pages)
print(number_of_pages)

# ページの取得
pdfReader.pages
print(pdfReader.pages)

# 1ページ目を取得する。
pageObj = pdfReader.pages[0]

# テキストの抽出
pageObj.extract_text()
print(pageObj.extract_text())

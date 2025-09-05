#! python3
# combinePdfs.py - カレントディレクトリの全PDFを1つのPDFに結合する

import pypdf, os  # ❶

# すべてのPDFファイル名を取得する
pdf_filenames = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_filenames.append(filename)  # ❷
pdf_filenames.sort(key=str.lower)  # ❸

writer = pypdf.PdfWriter()  # ❹

# すべてのPDFファイルをループする
for pdf_filename in pdf_filenames:
    reader = pypdf.PdfReader(pdf_filename)
    # 先頭を除くすべてのページをループして追加する
    writer.append(pdf_filename, (1, len(reader.pages)))

# 結合したPDFをファイルに保存する
with open('combined.pdf', 'wb') as file:
    writer.write(file)

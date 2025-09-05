import pypdf
writer = pypdf.PdfWriter()
writer.append('meetingminutes.pdf')
watermark_page = pypdf.PdfReader('watermark.pdf').pages[0]

for page in writer.pages:
    page.merge_page(watermark_page, over=False)

with open('with_watermark.pdf', 'wb') as file:
    writer.write(file)

import pypdf
writer = pypdf.PdfWriter()
writer.append('meetingminutes.pdf')
for i in range(len(writer.pages)):
    writer.pages[i].rotate(90)

with open('rotatedPage.pdf', 'wb') as file:
    writer.write(file)

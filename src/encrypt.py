import pypdf
writer = pypdf.PdfWriter()
writer.append('meetingminutes.pdf')
writer.encrypt('swordfish', algorithm='AES-256')
with open('encrypted.pdf', 'wb') as file:
    writer.write(file)

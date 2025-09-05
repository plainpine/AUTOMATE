import pypdf
writer = pypdf.PdfWriter()
writer.append('meetingminutes.pdf')
writer.append('meetingminutes2.pdf')
with open('combinedminutes.pdf', 'wb') as file:
    writer.write(file)
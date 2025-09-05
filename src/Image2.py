from PIL import Image
catIm = Image.open('zophie.png')
catIm.size
print(catIm.size)

width, height = catIm.size
width
print(width)

height
print(height)

catIm.filename
print(catIm.filename)

catIm.format
print(catIm.format)

catIm.format_description
print(catIm.format_description)

catIm.save('zophie.jpg')

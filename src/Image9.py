from PIL import Image
catIm = Image.open('zophie.png')

catIm.rotate(6).save('rotated6.png')
catIm.rotate(6, expand=True).save('rotated6_expanded.png')

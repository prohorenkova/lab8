from PIL import Image

im = Image.open('1.jpg')
im.crop((5, 50, 95, 200)).save('2.jpg')

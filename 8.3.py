from PIL import Image, ImageDraw, ImageFont

n = input("Введите имя получателя: ")
im = Image.open('33.jpg')
f = ImageFont.truetype("RifficFree-Bold.ttf", 80)
draw = ImageDraw.Draw(im)
draw.text((100, 90), n + ", от всего сердца, ", font=f, fill="#161a1e")
im.show()
im.save(n + 'otkrtka.png')

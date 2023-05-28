from PIL import Image

c = {1: 'dr.jpg', 2: 'ngod.png', 3: 'trud.jpg', 4: 'russia.jpg', 5: 'santex.jpg'}

print(" С Днём рождения -- 1\n", "С Новым годом -- 2\n", "С днём труда -- 3\n", "С днём России -- 4\n",
      "С Днём Сантехника -- 5")
a = int(input("Для получения открытки введите число - номер прадника : "))
im = Image.open(c[a])
im.show()

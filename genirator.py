from PIL import Image , ImageDraw , ImageFont
print ("Генератор мемов запущен!")
text = input("Ввидите 1 если нужен нужет только нижний или 2 если нужен и верхний и нежний текст")
top_text = ""
bottom_text = ""
if text == "1":
    bottom_text = input("Ввидите нижний текст")
elif text == "2":
    top_text = input("Ввидите верхний текст")
    bottom_text = input("Ввидите нижний текст")
else:
    print("Вы ввели не правельный символ попробуйте ещё раз")
print(bottom_text , top_text) 
meme = ["Кот в очках.png" , "Кот в ресторане.png"] 
print("Выберете картинку для мема: ")
for i in range(len(meme)):
    print(i, meme[i])

image = Image.open (meme[int(input("Выберете картинки:"))])
w , h = image.size
draw = ImageDraw.Draw (image)
font = ImageFont.truetype ("arial.ttf" , size=70) 
text = draw.textbbox((0 , 0), top_text, font)
text_1 = draw.textbbox((0 , 0), bottom_text, font)
draw.text(((w - text[2])/ 2, 10), top_text, font=font, fill="black")
draw.text(((w - text_1[2])/ 2, h - text[3]- 10), bottom_text, font=font, fill="black")
image.save ("New meme.png")
from PIL import Image, ImageDraw

canvas_width = 800
canvas_height = 400
canvas = Image.new("RGB", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(canvas)
step = 9
bar_height = 350
empty_space_top = 150
empty_space_bottom = 250

def get_bar_width(char):
    char = char.lower()
    if char.isalpha():
        position = ord(char) - ord('a') + 1
        return position
    else:
        return 1

input_string = "Raghu Vamsi Sai"
for x in input_string:
    get_bar_width(x)
x = step
for char in input_string:
    bar_width = get_bar_width(char)
    if char.isalpha():
        draw.rectangle([(x, 10), (x + bar_width, bar_height)], fill="black")
        x += bar_width + step
    if char ==" ":
        draw.rectangle([(x, empty_space_top), (x, empty_space_bottom)],fill="black")
        x += bar_width + step
canvas.save("output.png")
canvas.show()
import PIL
from PIL import Image
import requests
from io import BytesIO
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
import time

def get_color_list(color):
    color = str(color)
    color_code = color.replace(" ", "")
    color_code = color_code.replace("(", "")
    color_code = color_code.replace(")", "")
    color_code = color_code.split(",")
    color_list = [color_code[0], color_code[1], color_code[2]]
    return color_list

URL = "https://i.imgur.com/FBwTnLo.jpg"
response = requests.get(URL)
img = Image.open(BytesIO(response.content))

x_amount = img.width
y_amount = img.height
print(x_amount)
print(y_amount)

image_color_matrix = []

for y in range(0, img.height):
    image_color_matrix.append([])
    print("At line: " + str(y))
    for x in range(0, img.width):
        current_pixel = img.getpixel((x,y))
        current_color = get_color_list(current_pixel)
        image_color_matrix[y].append(current_color)

file = open("script.txt", "w")

code = ""
code += 'local model = Instance.new("Model")\n'
code += 'model.Parent = workspace\n\n'
for y in range(0, len(image_color_matrix)):
    print("Writing code from line " + str(y) + " of the matrix")
    for x in range(0, len(image_color_matrix[y])):
        current_rgb = image_color_matrix[y][x]
        code += 'x = Instance.new("Part")\n'
        code += 'x.Size = Vector3.new(1, 1, 1)\n'
        code += 'x.Parent = model\n'
        code += 'x.Anchored = true\n'
        code += 'x.Color = Color3.fromRGB(' + str(current_rgb[0]) + ', ' + str(current_rgb[1]) + ', ' + str(current_rgb[2]) + ')\n'
        code += 'x.Position = Vector3.new(' + str(x) + ', ' + str(y) + ', 0)\n\n'
        file.write(code)
        code = ""

file.close()

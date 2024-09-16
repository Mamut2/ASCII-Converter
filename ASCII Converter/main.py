import PIL.Image
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from termcolor import colored, cprint

clear = lambda: os.system('cls')

ASCII_CHARS = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', '\'', '.', ' ']
COLOR_TO_TEXT = ["black", "green", "red", "yellow", "blue", "cyan", "magenta", "white", "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan"]
#COLOR_TO_TEXT = ["black", "white"]

def resize_image(image, new_width = 100):
    width, height = image.size
    ratio = height / width
    #new_height = int(new_width * ratio)
    #resize_image = image.resize((new_width, new_height))
    resize_image = image.resize((new_width, 200))
    return(resize_image)

def grayify(image):
    return(image.convert('L'))

def pixel_to_ascii(image):
    pixels = image.getdata()
    print(len(ASCII_CHARS))
    characters = "".join(ASCII_CHARS[pixel // 4] for pixel in pixels)
    return(characters)

def cga_quantize(image):
    pal_image = PIL.Image.new("P", (1,1))
    pal_image.putpalette( (0,0,0, 0,255,0, 255,0,0, 255,255,0, 0,0,255, 0,255,255, 255,0,255, 255,255,255, 192,192,192, 105,105,105, 255,127,127, 124,252,0, 255,255,224, 173,216,230, 238,130,238, 224,255,255) )
    #pal_image.putpalette( (0,0,0, 255,255,255) )
    return image.convert("RGB").quantize(palette=pal_image)

def get_color(image):
    colors = []
    pixels = image.getdata()
    for pixel in pixels:
        colors.append(COLOR_TO_TEXT[pixel])
    return(colors)


def main(new_width = 300):
    os.system('color')
    path = input("Enter image path: \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid path to an image.")

    resized_image = resize_image(image, new_width)
    new_image_data = pixel_to_ascii(grayify(resized_image))

    colors = get_color(cga_quantize(resized_image))

    pixel_count = len(new_image_data)
    for i in range(0, pixel_count, new_width):
        cprint('\n', end='')
        for j in range(0, new_width):
            cprint(new_image_data[i + j], colors[i + j], end = ' ')
    #plt.imshow(cga_quantize(resized_image))
    #plt.show()
main()
#!/usr/bin/env python3
from typing import Tuple, NewType
from PIL import Image
from sys import argv


Pixel = NewType("Pixel", Tuple[int, int, int, int])

CHARACTERS = (' ', '.', '°', '*', 'o', 'O', '#', '@')

MAX_CHANNEL_INTENSITY = 255
MAX_CHANNEL_VALUES = MAX_CHANNEL_INTENSITY * 4 # 4 is the number of channels of a Pixel

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ASCII Art</title>
</head>
<body>
    <div style="background-color: black; color: white; line-height: 10px">
        <pre>{}</pre>
    </div>
</body>
</html>
"""


def map_intensity_to_character(intensity: float) -> CHARACTERS:
    return CHARACTERS[round(intensity * len(CHARACTERS))]


def get_pixel_intensity(pixel: Pixel) -> float:
    return sum(pixel) / 1020 # 1020 = 255 * 4


def print_ascii_art(size: Tuple[int, int], characters: str):
    index = 0
    for _ in range(size[1]):
        print(characters[index:index+size[0]])
        index += size[0]


def ascii_image_to_html(image_name: str, characters: str, size: Tuple[int, int]):
    with open(image_name + '.html', 'w') as image_file:
        ascii_image = ''    
        index = 0
        for _ in range(size[1]):
            ascii_image += characters[index:index+size[0]] + '\n'
            index += size[0]
        image_file.write(HTML_TEMPLATE.format(ascii_image))


def convert_image(image: Image) -> str:
    ascii_string = ''
    for pixel in image.getdata():
        intensity = get_pixel_intensity(pixel)
        character = map_intensity_to_character(intensity)
        ascii_string += character
    return ascii_string


def main() -> None:

    image_name = argv[1]
    image = Image.open(image_name)

    print(image.size, image.mode, image.size, image.getcolors())

    ascii_image = convert_image(image)

    #print_ascii_art(image.size, ascii_image)

    ascii_image_to_html(image_name, ascii_image, image.size)


if __name__ == '__main__':
    main()

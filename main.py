#!/usr/bin/env python3
from typing import Tuple, NewType
from PIL import Image


Pixel = NewType("Pixel", Tuple[int, int, int, int])

CHARACTERS = (' ', '.', '°', '*', 'o', 'O', '#', '@')

MAX_INTENSITY = 255


def map_intensity_to_character(intensity) -> CHARACTERS:
    return CHARACTERS[intensity * len(CHARACTERS) // MAX_INTENSITY]


def get_pixel_intensity(pixel: Pixel):
    return sum(pixel) // 1020 # 255 * 4


def main() -> None:

    IMAGE_NAME = 'image.jpg'
    image = Image.open(IMAGE_NAME)

    print(image.size, image.mode, image.size, image.getcolors())

    
    for pixel in image.getdata():
        intensity = get_pixel_intensity(pixel)
        character = map_intensity_to_character(intensity)
        print(f'{intensity=}, {character=}, {pixel=}', end='\t')

    # image.show()


if __name__ == '__main__':
    main()

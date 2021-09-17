#!/usr/bin/env python3
from typing import Tuple, NewType
from PIL import Image
from sys import argv

Pixel = NewType("Pixel", Tuple[int, int, int, int])

CHARACTERS = (' ', '.', '°', '*', 'o', 'O', '#', '@')

MAX_INTENSITY = 255


def map_intensity_to_character(intensity) -> CHARACTERS:
    return CHARACTERS[intensity]


def get_pixel_intensity(pixel: Pixel):
    return round(sum(pixel) / 1020 * len(CHARACTERS)) # 1020 = 255 * 4


class Printer:

    def __init__(self, size: Tuple[int, int], chars: str) -> None:
        self.size = size
        self.chars = chars

    def print(self) -> None:
        #print(self.chars)
        index = 0
        for _ in range(self.size[1]):
            print(self.chars[index:index+self.size[0]])
            index += self.size[0]


class Counter:

    def __init__(self) -> None:
        self.nums = {}
    
    def count(self, num):
        if num in self.nums.keys():
            self.nums[num] += 1
        else:
            self.nums[num] = 1
    
    def results(self):
        for key, value in self.nums.items():
            print(f'Key: {key}, value: {value}')


def main() -> None:

    IMAGE_NAME = argv[1]
    image = Image.open(IMAGE_NAME)

    print(image.size, image.mode, image.size, image.getcolors())

    counter = Counter()
    
    chars = ''
    for pixel in image.getdata():
        intensity = get_pixel_intensity(pixel)
        character = map_intensity_to_character(intensity)
        chars += character
        #print(intensity)
        counter.count(character)
        #print(character)
        #print(f'{intensity=}, {character=}, {pixel=}', end='\t')

    # image.show()
    printer = Printer(image.size, chars)
    printer.print()
    counter.results()


if __name__ == '__main__':
    main()

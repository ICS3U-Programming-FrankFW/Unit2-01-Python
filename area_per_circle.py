#!/usr/bin/env python3
# Created By: Frankie Fox Wagoosh
# Date: Sept 22, 2022
# This program calculates the area and perimeter of a circle with a radius of 15mm.
import math


def main():
    print(
        "This program calculates the area and perimeter of a circle with a radius of 15mm."
    )
    radius = 15

    # calculate the circumference and area
    circumference = math.pi * 2 * radius
    area = math.pi * radius**2

    # display the area and circumference
    print("The area is {}".format(area))
    print("The circumference is {}".format(circumference))


if __name__ == "__main__":
    main()

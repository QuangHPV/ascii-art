from PIL import Image
import numpy as np

with Image.open("images/boat.jpg") as im:
    # Load image
    print("Successfully loaded image!")
    width, height = im.size
    print(f"Image size: {width} x {height}")

    # Ensure format is RGB
    im = im.convert("RGB")

    # extract pixel data
    pixels = list(im.getdata())
    # Numpy 2d array
    pixels = np.array(pixels)
    pixels = pixels.reshape((height, width, 3))
    tuple_pixels = []
    for row in pixels:
        tuple_row = []
        for pixel in row:
            tuple_row.append(tuple(pixel))
        tuple_pixels.append(tuple_row)

    
    
    # Iterating through pixel
    print("Iterating through an upper left portion of the pixel matrix:")

    for row in tuple_pixels[:10]:
        for pixel in row[:10]:
            print(f"{pixel}", end=" ")
        print()
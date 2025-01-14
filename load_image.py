from PIL import Image
import numpy as np

with Image.open("images/boat.jpg") as im:
    # Load image
    print("Successfully loaded image!")
    width, height = im.size
    print(f"Image size: {width} x {height}")


    
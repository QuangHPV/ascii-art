from PIL import Image

with Image.open("images/boat.jpg") as im:
    print("Successfully loaded image!")
    print(f"Image size: {im.size[0]} x {im.size[1]}")
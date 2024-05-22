from PIL import Image
import numpy as np

def main():
    pixels = extract_pixel()
    # Iterating through pixel
    print("Iterating through an upper left portion of the pixel matrix:")

    for row in pixels[:10]:
        for pixel in row[:10]:
            print(f"{pixel}", end=" ")
        print()
    
    # Iterating through brightness pixels
    brightness = to_brightness(pixels)
    for row in brightness[300:350]:
        for pixel in row[200:250]:
            print(f"{pixel}", end=" ")
        print()



def extract_pixel():
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

        return tuple_pixels



def linearize(v):
    if v <= 0.04045:
        return v / 12.92
    else:
        return ((v + 0.055) / 1.055) ** 2.4
    
def yToLStar(y):
    if y <= 0.008856:
        return y * 903.3
    else:
        return (y ** (1/3)) * 116 - 16

def to_brightness(pixels):
    """ 
    Convert gamma encoded RGB values to linear values, then computer luminance for each tuple

    Parameters: 
    pixels: 
    Return
    luminance:
    """
    lightness = []
    for row in pixels:
        l_row = []
        for pixel in row:
            r, g, b = pixel
            r_lin, g_lin, b_lin = linearize(r / 255), linearize(b / 255), linearize(g / 255) 
            l_star = yToLStar(r_lin * 0.2126 + g_lin * 0.7152 + b_lin * 0.0722)
            l_row.append(int(l_star * 255 / 100))
        lightness.append(l_row)
    return lightness    



if __name__ == "__main__":
    main()
            

    

    



    
from PIL import Image
import numpy as np

def main():
    pixels = extract_pixel("images/ascii-pineapple.jpg")
    
    # Iterating through brightness pixels
    brightness = to_brightness(pixels)
    
    # to ascii art
    ascii = to_ascii(brightness)
    for row in ascii:
        print(row)





def extract_pixel(path):
    with Image.open(path) as im:
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
    brightness = []
    for row in pixels:
        l_row = []
        for pixel in row:
            r, g, b = pixel
            #r_lin, g_lin, b_lin = linearize(r / 255), linearize(b / 255), linearize(g / 255) 
            #l_star = yToLStar(r_lin * 0.2126 + g_lin * 0.7152 + b_lin * 0.0722)
            l_row.append(int(r * 0.2126 + g * 0.7152 + b * 0.0722))
        brightness.append(l_row)
    return brightness    

def to_ascii(brightness):
    s = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    s = s[::-1]
    #s = " .:-=+*#%@"
    # Divide 256 brightness value into 72 region 
    ascii = []
    for row in brightness:
        a_row = ""
        for pixel in row:
            a_row += s[int(pixel * 69 / 255)] * 2
        ascii.append(a_row)
    
    return ascii




if __name__ == "__main__":
    main()
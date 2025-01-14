# ASCII Art
## Usage
Modify the directory to image in the to_acsii.py script  
```python
from PIL import Image
import numpy as np

def main():
    pixels = extract_pixel(your_image_directory)
    
    # Iterating through brightness pixels
    brightness = to_brightness(pixels)
```
Then, run it in terminal to get the ascii art
```
python to_ascii.py
```
## Tools
- Pillow
## Development plan
- Testing on various image size and resolution
- Argument passing
- More options in image transfomation (colours, styles, etc.)
- GUI
- Web-based


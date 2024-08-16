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
...
```
Then, run it in terminal to get the ascii art
```
python to_ascii.py
```
## Tools
- PILLOW
## Development plan
- Argument passing
- GUI
- Web-based
- Tweaks in image transfomation

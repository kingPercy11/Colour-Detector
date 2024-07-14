# Color Detection

Color Detection is a simple Python script that allows you to detect specific colors in an image using OpenCV. You can specify the hue, saturation, and value (brightness) ranges to create a mask that highlights the desired color.

## Features
- Detect specific colors in an image based on HSV color space.
- Customize the hue, saturation, and value ranges for color detection.

## Prerequisites
- Python 3.x
- OpenCV

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/color-detection.git
    cd color-detection
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python
    ```

## Usage
1. Run the script:
    ```bash
    python color_detection.py
    ```

2. Follow the prompts to enter the input image path and specify the hue, saturation, and value ranges.

Example:
```bash
Enter the image path: path/to/your/image.jpg
Enter lower hue value (0-179): 30
Enter upper hue value (0-179): 90
Enter lower saturation value (0-255): 50
Enter upper saturation value (0-255): 255
Enter lower value (brightness) value (0-255): 50
Enter upper value (brightness) value (0-255): 255

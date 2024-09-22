import cv2
import numpy as np
import os


def upscale_image(image_path, output_name, scale_factor):
    image = cv2.imread(image_path)
    new_size = (int(image.shape[1] * scale_factor), int(image.shape[0] * scale_factor))
    upscaled_image = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)

    # Save the image to the desktop
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    output_path = os.path.join(desktop, output_name)
    cv2.imwrite(output_path, upscaled_image)


# Example usage
upscale_image('/Users/yusufkoksal/Desktop/deneme.jpg', '/Users/yusufkoksal/Desktop/deneme_upscaled.jpg', 2)

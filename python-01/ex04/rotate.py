import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import sys


# function that takes an image as input and displays it,
# then crops it to a square of size 400x400 pixels,
# and finally displays the cropped image in grayscale.
# rotate it by 90 degrees and display it.
# The function should display the original image and the cropped image
# in two separate windows.
# The function should also print the shape of the original
# image and the shape of the cropped image in the console.
def rotate(image):
    try:
        img = Image.open(image)
        print(ft_load(image))
        # Define the crop rectangle
        left = 400
        upper = 100
        size = 400  # size of the square
        zoomed_img = img.crop((left, upper, left + size, upper + size))

        print("no color image shape: ")
        gray_img = zoomed_img.convert("L")
        width, height = gray_img.size
        new_gray_img = Image.new("L", (height, width))
        for x in range(width):
            for y in range(height):
                pixel = gray_img.getpixel((x, y))
                new_gray_img.putpixel((y, width - x - 1), pixel)
        gray_img.show()

        print("New shape after cropping:", np.array(gray_img).shape)
        print(np.array(gray_img))

        plt.imshow(new_gray_img, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except FileNotFoundError:
        print("The image file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    rotate(sys.argv[1])


if __name__ == "__main__":
    main()

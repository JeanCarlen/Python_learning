import numpy as np
from PIL import Image
from load_image import ft_load
import matplotlib.pyplot as plt
import sys


# function that takes an image as input and displays it,
# then crops it to a square of size 400x400 pixels,
# and finally displays the cropped image in grayscale.
# The function should display the original image and the cropped image
# in two separate windows.
# The function should also print the shape of the original
# image and the shape of the cropped image in the console.
def zoomin(image):
    try:
        img = Image.open(image)
        print(ft_load(image))
        img.show()
        # Define the crop rectangle
        left = 400
        upper = 100
        size = 400  # size of the square
        zoomed_img = img.crop((left, upper, left + size, upper + size))

        zoomed_img.show()
        # zoomed_img.save("zoomed_img.jpeg")
        # print("color image shape: ")
        # print("New shape after cropping: ", np.array(zoomed_img).shape)
        # print("New shape after slicing: \n", np.array(zoomed_img))
        print("no color image shape: ")
        gray_img = zoomed_img.convert("L")
        gray_img.show()
        gray_img_arr = np.expand_dims(np.array(gray_img), axis=-1)
        print(f"New shape after cropping: {gray_img_arr.shape}")
        print(gray_img_arr)

        plt.imshow(gray_img, cmap='gray')
        plt.title("Zoomed Image")
        plt.axis('on')
        plt.show()

    except FileNotFoundError:
        print("The image file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    zoomin(sys.argv[1])


if __name__ == "__main__":
    main()

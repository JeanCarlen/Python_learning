import numpy as np
from PIL import Image


# function that loads an image from a file into a numpy array
# and prints its shape and returns the array
def ft_load(path: str) -> np.array:
    try:
        if type(path) is not str:
            raise TypeError("Path must be a string")
        if path == "":
            raise ValueError("Path must not be empty")
        if not path.endswith(".jpg") and not path.endswith(".jpeg"):
            raise ValueError("Path must be a .jpg or .jpeg file")
        image = np.array(Image.open(path))
        print("The shape of the is : ", image.shape)

        return np.array(image)

    except Exception as e:
        print(e)
        return ""

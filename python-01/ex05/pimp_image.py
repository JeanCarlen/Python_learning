from PIL import Image


def ft_invert(array):
    # Invert color by subtracting color values from 255
    """Inverts the color of the image received."""
    img = 255 - array
    Image.fromarray(img).show()
    return img


def ft_red(array):
    # Keep only the red channel
    img = array.copy()
    img[:, :, 1] = img[:, :, 2] = 0
    Image.fromarray(img).show()
    return img


def ft_green(array):
    # Keep only the green channel
    img = array.copy()
    img[:, :, 0] = img[:, :, 2] = 0
    Image.fromarray(img).show()
    return img


def ft_blue(array):
    # Keep only the blue channel
    img = array.copy()
    img[:, :, 0] = img[:, :, 1] = 0
    Image.fromarray(img).show()
    return img


def ft_grey(array):
    # Convert to grayscale by taking the mean of the color channels
    img = (array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3)
    Image.fromarray(img).show()
    return img

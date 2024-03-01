import numpy as np


# function that take a list of list, truncate it and return the new list
def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list):
            raise TypeError("Family must be a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and end must be integers")
        if (len(family) == 0):
            return "Family is empty"
        width = len(family[0])
        for row in family:
            if type(row) is not list:
                raise AssertionError("Family must be a list of lists")
            if len(row) != width:
                return AssertionError("Family is not a rectangle")

        shape = np.array(family).shape

        print("My shape is : ", shape)

        new_family = np.array(family[start:end])

        second_shape = new_family.shape

        print("My new shape is : ", second_shape)
        return new_family.tolist()

    except Exception as e:
        print(e)
        return ""

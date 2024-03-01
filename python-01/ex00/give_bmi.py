# function that take two list of int or float and return a bmi list
def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    try:
        if len(height) != len(weight):
            raise ValueError(
                "Height and weight lists must be of the same length")

        bmi_list = []

        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or \
                    not isinstance(w, (int, float)):
                raise ValueError(
                    "All elements in lists must be int or floats")
            if h <= 0 or w <= 0:
                raise ValueError(
                    "All elements in lists must be positive")
            bmi = w / (h ** 2)
            # print("h = ", h, "/w = ", w)
            # print(w / (h ** 2))
            bmi_list.append(bmi)
        return bmi_list
    except Exception as e:
        print("Give_bmi Error: ", e)
        return []


# function that take the bmi list with a
# limit and return a list of boolean(true or false)
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        new_list = []
        # print("bmi = ", bmi)
        if not isinstance(limit, int) and not isinstance(limit, float):
            raise TypeError("Limit must be an int or a float")
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise ValueError("All elements in list must be int or floats")
            # print("value =", value)
            new_list.append(value > limit)
            # print("new_list = ", new_list)
        return new_list
    except Exception as e:
        print("Apply limit Error: ", e)
        return []

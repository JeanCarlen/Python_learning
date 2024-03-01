def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : None <class 'NoneType'>")
    elif object != object:
        print("Cheese: nan <class 'float'>")
    elif object == 0:
        print("Zero: 0 <class 'int'>")
    elif object == "":
        print("Empty: <class 'str'>")
    elif object is False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not Found")
    return (1)

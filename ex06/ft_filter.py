def ft_filter(function, iterable):
    if (iterable is None):
        return None
    if (function is None):
        return [i for i in iterable if i]
    return [i for i in iterable if function(i)]

# passe une fonction sur chaque element de la liste(iterable)
# et retourne une liste des elements qui ont retourné True



ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print("before changement")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

ft_list[0] = "Hello"
ft_list[1] = "World!"


ft_tuple = list(ft_tuple)
ft_tuple[0] = "Hello"
ft_tuple[1] = "France!"
ft_tuple = tuple(ft_tuple)

ft_set.remove("Hello")
ft_set.remove("tutu!")
ft_set.add("Hello")
ft_set.add("Paris")


ft_dict["Hello"] = "42 Paris!"


print("\nAfter changement")
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

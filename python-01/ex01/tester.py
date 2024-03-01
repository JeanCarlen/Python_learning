from array2D import slice_me

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print("Normal case: ", family)
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print()

family = [[1.80, 78.4], [2.15, 102.7, 1], [2.10, 98.5], [1.88, 75.2]]
print("Not rectangle case: ", family)
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print()

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], 1]
print("Not rectangle case: ", family)
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print()

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print("Out of range case: ", family)
print(slice_me(family, 0, 10))
print(slice_me(family, 1, -10))
print()

print("Not list case: ", 1, "test test test")
print(slice_me(1, 0, 2))
print(slice_me("test test test", 1, -2))
print()

family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print("End < start case: ", family)
print(slice_me(family, 2, 1))
print(slice_me(family, -2, -3))

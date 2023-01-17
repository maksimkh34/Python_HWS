import numpy as np

arr = np.array(
    [[2, 0, 6],
    [4, 9, 5],
    [3, 5, 8]]
)
arr2 = np.linspace(3, 1, 9)
arr2 = arr2.reshape(3, 3)
print(arr)
print()
print(arr2)

print("\nsum:")
print(arr + arr2)

print("\nmul:")
print(arr * arr2)

print("\ndiv:")
print(arr / arr2)


print(f"max: {arr.max(axis=0)}")
print(f"max2: {arr.max(axis=1)}")


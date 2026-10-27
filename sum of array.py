n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

total = 0

for value in arr:
    total += value

print("Array elements:", arr)
print("Sum of array elements:", total)

n = int(input("Enter number of terms: "))

a = 0
b = 1

if n < 0:
    print("Enter a non-negative number.")
else:
    for i in range(n):
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num

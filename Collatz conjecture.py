import math

n = int(input("Your number: "))
j = 0

while n != 1:
    if (divmod(n, 2)[1] == 0):
        print(n)
        n = n/2
        j = j + 1
    else:
        print(n)
        n = (3 * n) + 1
        j = j + 1
print(n)
print("It took " + str(j) + " steps")
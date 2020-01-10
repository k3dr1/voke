eps = int(input("Enter the number: ")) - 1
x = 1
y = 1
if (eps + 1) == 1:
    print("F(" + str(1) + ") is " + str(1))
elif (eps + 1) == 2:
    print("F(" + str(1) + ") is " + str(1))
    print("F(" + str(2) + ") is " + str(2))
else:
    print("F(" + str(1) + ") is " + str(1))
    for f in range(eps):
       print("F(" + str(f + 2) + ") is " + str(x))
       x=x+y
       y=x-y

input()
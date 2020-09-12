#This is a little Python code to compute the numerical solutions
#for IVPs

#slope_given = f(x, y)
#initial_values = (y(n) = m)
#h = step size

import re
from matplotlib import pyplot as plt

point_number = 350
h = 0.01

def calculate_slope(x, y):
    slope = slope_given
    slope.replace("x", str(x))
    slope.replace("y", str(y))
    return eval(slope)

print("Give a f(x, y) in a differential equation dy/dx = f(x, y)")
slope_given = input()
print("Initial values (in form of y(n)=m)")
initial_values = input()
initial_values = initial_values.replace(" ", "")

x = float(re.findall("\(.*\)", initial_values)[0][1:-1])
y = float(re.findall("\=.*", initial_values)[0][1:])

x_values = []
y_values = []

for _ in range(1, point_number + 1):
    x_values.append(x)
    y_values.append(y)
    slope = calculate_slope(x, y)
    x = x + h
    y = y + h*slope

plt.plot(x_values, y_values)
plt.show()
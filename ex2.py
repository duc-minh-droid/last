

from math import sqrt


a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

delta = b**2 - (4*a*c)
x = 0
if delta < 0:
    print("This equation has no solution")
elif delta == 0:
    x = - b / (2*a)
    print(f"This equation has a double solution x = {x}")
else:
    x1 = (-b+sqrt(delta))/(2*a)
    x2 = (-b-sqrt(delta))/(2*a)
    print(f"This equation has two solutions x = {x1} and x = {x2}")
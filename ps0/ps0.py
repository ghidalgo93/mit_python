import numpy as np

# Ask user for input
x: int = int(input("Enter number x: "))
y: int = int(input("Enter number y: "))

pwr: int = int(x**y)
log: int = int(np.log(x))

print("X**y = " + str(pwr))
print("log(x) = " + str(log))






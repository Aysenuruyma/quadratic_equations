import math
import matplotlib.pyplot as plt
import numpy as np

print ("lets investigate the roots of a quadratic equations as y= ax^2 + bx + c")
a = int (input("a : "))
b = int (input("b : "))
c = int (input("c : "))

disc = b**2 - 4*a*c

print ("the discriminant: ",disc)

x1 = (-b + math.sqrt(disc))/2*a
x2 = (-b - math.sqrt(disc))/2*a

if disc > 0:
    print ("there are 2 reel roots")
    print ("the roots: ", x1, x2)
elif disc == 0:
    print ("there is 1 reel root")
    print ("the root: ", x1)
else:
    print ("there is no reel root")


x1 = np.linspace(-10,10)
##print (x1)
##x2 = np.linspace(-10,10)

y1 = a*(x1**2) + b*x1 + c
##print (y1)


##fig, ax = plt.subplots()
##ax.plot(x1, y1)

plt.plot(x1,y1)
plt.show()


##plt.plot ([x1, a*(x1**2) + b*x1 + c],[x2, a*(x2**2) + b*x2 + c])
##plt.show()

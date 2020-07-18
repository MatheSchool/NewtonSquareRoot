def F(x):      # Function
    return x**2 - 2
 
def dFdx(x):   # Derivative function
    return 2*x


rootValues = [4.0] # Initial value
error = 0.001
rootGuess = rootValues[-1]
print("%11s %11s" % ("x", "F(x)"))
while True:
    print("%11.8f %11.8f" % (rootGuess, F(rootGuess)))
    droot = -1*F(rootGuess)/dFdx(rootGuess)
    rootGuess = rootGuess + droot
    rootValues.append(rootGuess)
    if abs(rootValues[-2] - rootValues[-1]) < error:
        break
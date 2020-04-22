import sys
from engineering_notation import EngNumber

# Python tool for calculating possible RC combinations to obtain a desired
# RC product.
# 1st argument is a lower bound on the range of R*C
# 2nd argument is an upper bound on the range.

lowerBound = float(sys.argv[1])
upperBound = float(sys.argv[2])

R = []
C = []
solList = []
rValues = [1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8,
        2.0, 2.2, 2.4, 2.7, 3.0, 3.3,
        3.6, 3.9, 4.3, 4.7, 5.1, 5.6,
        6.2, 6.8, 7.5, 8.2, 9.1]
cValues = [2.2,3.3,4.7,6.8,
        10,12,15,18,22,27,33,39,47,56,68,82]
cValuesLarge = [10,15,22,33,47,68]

for n in range(0,9):
    for r in rValues:
        r = r*10**n
        if r not in R:
            R.append(float('%.3g' % r)) # Round to 3 sig figs

for n in range(-12,-6):
    for c in cValues:
        c = c*10**n
        if c not in C:
            C.append(float('%.3g' % c))

for n in range(-6,-2):
    for c in cValuesLarge:
        c = c*10**n
        if c not in C:
            C.append(float('%.3g' % c))

for r in R:
    print(r)
for c in C:
    print(c)

for r in R:
    for c in C:
        if r*c >= lowerBound and r*c <= upperBound and [r,c] not in solList:
            print("R = %-*s C = %-*s" % \
                    (5,EngNumber(r),5,EngNumber(c)),\
                    "gives RC =","{:.2e}".format(r*c))
            solList.append([r,c])

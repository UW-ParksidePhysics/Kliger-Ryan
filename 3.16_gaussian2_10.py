from math import sqrt, exp, pi
def gauss(x, m=0, s=1):
    return 1 / sqrt((2 * pi) * s) * exp(-1/2*((x - m)/s) ** 2)
m = 5
s = 1
n = 6

print("      + |  gauss(x) ")
print("-------+----------")
for x in [m - 5*s + i*(10 * s /(n - 1)) for i in range(n)]:
    print((f" {x:5.6f} | {gauss(x, m, s):5.7e} "))
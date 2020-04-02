from math import sin, cos, pi

x = pi/4
val = sin(x)**2 + cos(x)**2
print(val)

v0 = 3
t = 1
a = 2
s = v0*t + 0.5*a*t**2
print(s)

a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a**2 + 2*a*b + b**2
eq2_sum = a**2 - 2*a*b + b**2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print("First equation: {:g}={:g}" .format(eq1_sum, eq1_pow))
print("Second equation: {:g}={:g}" .format(eq2_pow, eq2_pow))
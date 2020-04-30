import sys


try:
    F = float(sys.argv[1])
except:
    F = float(input('Temperature in degrees Fahrenheit?'))

C = 5/9. * (F - 32)
print("%g Fahrenheit = %g Celsius" %(F, C))

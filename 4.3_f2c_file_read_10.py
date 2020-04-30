infile = open('temperature.dat', 'r')
for i in range(0, 3):
    infile.readline()

F = float(((infile.readline()).split())[2])
infile.close()
C = (5/9) * (F - 32)
print(C)
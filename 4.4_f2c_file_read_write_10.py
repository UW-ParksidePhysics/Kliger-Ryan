infile = open('temperature2.dat', 'r')
for i in range(0, 3):
    infile.readline()
for line in infile:
    F = float(line.split()[2])
    C = (5/9) * (F - 32)
    print('%f %f' %(F, C))
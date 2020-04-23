def read_constants(filename):
    infile = open(filename, 'r')
    constants = {}
    infile.readline()
    infile.readline()
    for line in infile:
        name_of_constant = ' '.join(line.split()[:-2])

        value = (line.split()[-2])

        constants[name_of_constant] = value

    infile.close()

    return constants


constants = read_constants('constants.py')
print('-------------------------------------')
print(constants)
print('-------------------------------------')
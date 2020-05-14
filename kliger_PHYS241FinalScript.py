import statistics

import two_column_text_read_10 as tctr
import plot_data_with_fit_10
import lowest_eigenvectors_10
import univariate_statistics_10 as us
import fit_curve_array_10
import quadratic_fit_10 as qf
import matplotlib.pyplot as plt
import equations_of_state as eos
import statistics as st
import numpy as np

filename = 'Sn.Fd-3m.GGA-PBEsol.volumes_energies.dat'
display_Graph = True
my_eos = 'Vinet'
potential_name = 'sinusoidal'
number_of_dimensions = 110
potential_parameter = 100

# 1.
# Extract...(C) chemical symbol, (S) crystal symmetry symbol, (A) approximation
def parse_file_name(filename):
    to_parse = filename.split('.')
    C, S, A = to_parse[0:3]
    print(to_parse[0:3])
    return C, S, A


C, S, A = parse_file_name(filename)

# 2.
data = tctr.two_column_text_read(filename)
print('Data Read In:')
print(data)

# 3.
data1 = data/2
print('Revised data from atoms:')
print(data1)

# 4.
statistics = us.univariate_statistics(data1)
print('Statistics of data:')
print(statistics)

# 5.
quadratic_coefficients = qf.quadratic_fit(data1)
print('Quadratic coefficients of revised data:')
print(quadratic_coefficients)

# 6.
volumes = data1[:,0]
energies = data1[:,1]
eos_passed_info, eos_parameters = eos.fit_eos(volumes, energies, quadratic_coefficients, my_eos, number_of_points=50)
print('Fitted Data/Quadratic Coefficients:')
print(eos_passed_info)
equilibrium_volume = eos_parameters[3]
bulk_modulus = eos_parameters[1]

# 7.
def convert_units(value_to_convert_from, units_of_value_converted_from, unit_to_convert_to):
    if units_of_value_converted_from == 'cubic bohr/atom':
        value_in_requested_units = value_to_convert_from * 0.148185
    elif units_of_value_converted_from =='rydberg/atom':
        value_in_requested_units = value_to_convert_from * 13.606
    elif units_of_value_converted_from == 'rydberg/cubic bohr':
        value_in_requested_units = value_to_convert_from / 29421.0265
    else:
        value_in_requested_units = unit_to_convert_to
    return value_in_requested_units

# 8.
eos_volumes = np.linspace(min(volumes), max(volumes), len(eos_passed_info))

print(eos_volumes)
plt.plot(volumes, energies, 'o', color='red')
plt.plot(eos_volumes, eos_passed_info, color='black')
x_min = (min(volumes) - (0.1) * (max(volumes) - min(volumes)))
x_max = (max(volumes) + (0.1) * (max(volumes) - min(volumes)))
y_min = (min(energies) - (0.1) * (max(energies) - min(energies)))
y_max = (max(energies) - (0.1) * (max(energies) - min(energies)))
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r' $V$ [eV/atom] ')
plt.ylabel(r' $E$ [$\AA^3$/atom] ')

# 9.
def annotate_graph(C, S, A, bulk_modulus, equilibrium_volume, x_min, x_max, y_min, y_max):
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_C = x_min + 0.05 * x_range
    y_C = y_max - 0.05 * y_range
    plt.text(x_C, y_C, C)













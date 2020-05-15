import statistics

import two_column_text_read_10 as tctr
import plot_data_with_fit_10
import lowest_eigenvectors_10 as le
import univariate_statistics_10 as us
import fit_curve_array_10
import quadratic_fit_10 as qf
import matplotlib.pyplot as plt
import equations_of_state as eos
import statistics as st
import numpy as np
import generate_matrix as gm

filename = 'Sn.Fd-3m.GGA-PBEsol.volumes_energies.dat'
display_Graph = True
display_graph2 = True
my_eos = 'vinet'
potential_name = 'sinusoidal'
number_of_dimensions = 110
potential_parameter = 100
minimum_x = 1
maximum_x = 400

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
print(bulk_modulus)

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
plt.plot(volumes, energies, 'o', color='blue')
plt.plot(eos_volumes, eos_passed_info, color='black')
x_min = (min(volumes) - (0.39) * (max(volumes) - min(volumes)))
x_max = (max(volumes) + (0.39) * (max(volumes) - min(volumes)))
y_min = (min(energies) - (0.39) * (max(energies) - min(energies)))
y_max = (max(energies) - (0.39) * (max(energies) - min(energies)))
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r' $V$ [eV/atom] ')
plt.ylabel(r' $E$ [$\AA^3$/atom] ')
plt.show()

# 9.
def annotate_graph(C, S, A, bulk_modulus, equilibrium_volume, x_min, x_max, y_min, y_max):
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_C = x_min + 0.05 * x_range
    y_C = y_max - 0.05 * y_range
    x_S = x_min + x_range/2
    y_S = y_max - y_range/2
    x_A = x_min + x_range/2
    y_A = ((y_max - y_range/2) + 0.0005)
    x_Eqv = (x_min + x_range/2)
    y_Eqv = ((y_max - y_range/2) - 0.004)
    print(A)
    plt.title('Vinet Equation of State for Sn', y=1.05)
    plt.text(x_C, y_C, C)
    print(S)
    plt.text(x_S, y_S, r' $ \ Fd}$3$m} $')
    plt.text(x_A, y_A, r' $A_0$ =0.0028354960426282324 GPa')
    print(equilibrium_volume)
    plt.text(x_Eqv, y_Eqv, r' $V_0 = 155.59 \AA^3/atom $')
    plt.figtext(0, 0, 'Created By Ryan Kliger 2020-05-14')
annotate_graph(C, S, A, bulk_modulus, equilibrium_volume, x_min, x_max, y_min, y_max)

# 10.
if display_Graph == True:
    plt.show(display_Graph)
elif display_Graph == False:
    plt.savefig('Sn.Fd-3m.GGA-PBEsol.png')


# 11.
square_matrix = gm.generate_matrix(minimum_x, maximum_x, number_of_dimensions, potential_name, potential_parameter)
print('Matrix Generated:')
print(square_matrix)

# 12.
eigenvalues, eigenvectors = le.lowest_eigenvectors(square_matrix, number_of_eigenvectors=3)
print('eigenvectors/eigenvalues:')
print(eigenvalues, eigenvectors)

# 13.
grid_of_spatial_points = np.linspace(-10, 10, number_of_dimensions)
print('Grid of Spatial Points:')
print(grid_of_spatial_points)

# 14.
plot1 = plt.plot(grid_of_spatial_points, eigenvectors[0][0:number_of_dimensions], color='red')
plot2 = plt.plot(grid_of_spatial_points, eigenvectors[1][0:number_of_dimensions], color='green')
plot3 = plt.plot(grid_of_spatial_points, eigenvectors[2][0:number_of_dimensions], color='blue')
plt.xlabel('x [a.u.]')
plt.ylabel(r' $\psi_n$(x)[a.u.]')
plt.legend((plot1, plot2, plot3), (r'$\psi_n$, $E_1$=(1)[a.u.]', r'$\psi_n$, $E_2$=(2)[a.u.]', r'$\psi_n$, $E_3$=(3)[a.u.]'))
plt.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])

# 15.
plt.axhline(color="black")

# 16.
plt.text(-9, -1.5,  "Created by Ryan Kliger 2020-05-14")

# 17.
plt.title('Select Wavefunctions for a Sinusoidal Potential on a Spatial Grid of 110 Points')

# 18.
if display_graph2 == True:
    plt.show(display_graph2)
elif display_graph2 == False:
    plt.savefig('Sinusoidal_Potential.png')






















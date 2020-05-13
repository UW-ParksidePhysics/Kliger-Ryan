import statistics

import two_column_text_read_10
import plot_data_with_fit_10
import lowest_eigenvectors_10
import univariate_statistics_10
import fit_curve_array_10
import quadratic_fit_10

filename = 'Sn.Fd-3m.GGA-PBEsol.volumes_energies.dat'

data = two_column_text_read_10.two_column_text_read(filename)
print(filename)

plot_data_with_fit_10.plot_data_with_fit(data, fit_curve=2, data_format=0, fit_format=0)

lowest_eigenvectors_10.square_matrix()

lowest_eigenvectors_10.lowest_eigenvectors(square_matrix=5, number_of_eigenvectors=3)
print(lowest_eigenvectors_10.lowest_eigenvectors)


# Fit an equation of state
def parse_file_name(filename, equations_of_state=3):
    print("Sn.Fd-3m.GGA-PBEsol")
    two_column_text_read_10.two_column_text_read(filename)
    print(two_column_text_read_10.two_column_text_read(filename))
    univariate_statistics_10.univariate_statistics(data)
    fit_curve_array_10.fit_curve_array(statistics)
    equations_of_state.fit_eos(quadratic_coefficients=3)


def convert_units(data):
    return data[0]/data[1]







'''
analyze_and_thermocline.py

Stephen Owusu Badu
Fall 2024
CS152 Project 4 Extension

This script performs the following tasks:
1. Analyzes a specified column of data from a CSV file (e.g., temperature).
2. Computes the mean, min, and max of the column, printing the corresponding days on which the min and max occur.
3. Computes the thermocline depth for the days with the minimum and maximum temperatures using temperature data from the same file.

To run this program, use the following command:
python3 analyze_and_thermocline_extension.py GoldieJulyNoon2019.csv 4
'''

import stats
import sys

# Function to compute density from temperature
def compute_density_from_temp(temp):
    return 1000 * (1 - (temp + 288.9414) * (temp - 3.9863)**2 / (508929.2 * (temp + 68.12963)))

# Function to compute densities from a list of temperatures
def compute_densities(temps):
    densities = []
    for temp in temps:
        densities.append(compute_density_from_temp(temp))
    return densities

# Function to compute density derivatives based on depth
def compute_density_derivatives(densities, depths):
    density_derivatives = []
    for i in range(len(densities) - 1):
        density_derivative = (densities[i+1] - densities[i]) / (depths[i+1] - depths[i])
        density_derivatives.append(density_derivative)
    return density_derivatives

# Function to compute the thermocline depth
def thermocline_depth(temps, depths):
    densities = compute_densities(temps)
    density_derivatives = compute_density_derivatives(densities, depths)
    max_derivative, max_index = stats.max(density_derivatives)
    return (depths[max_index] + depths[max_index + 1]) / 2

# Function to get temperatures for a specific day (thermo_day) and compute the thermocline
def compute_thermocline_for_day(thermo_day, filename):
    depths = [1, 3, 5, 7, 9, 11, 13, 15]
    depth_indices = [10, 11, 16, 17, 15, 14, 13, 12]

    fp = open(filename, "r")
    headers = fp.readline()
    day = 1

    for line in fp:
        if day == thermo_day:
            items = line.split(',')
            temperatures = [float(items[idx]) for idx in depth_indices]
            thermo_depth = thermocline_depth(temperatures, depths)
            print(f"Thermocline depth for day {thermo_day}: {thermo_depth:.2f} meters")
            break
        day += 1

    fp.close()

# Main function to analyze the data and compute thermoclines for the min and max days
def main(filename, column_index):
    fp = open(filename, 'r')
    header = fp.readline().split(',')
    print(header)

    data = []
    for line in fp:
        items = line.split(',')
        data.append(float(items[column_index]))

    mean = stats.compute_mean(data)
    print(f"Mean value for column {column_index}: {mean:.2f}")

    min_value, min_index = stats.min(data)
    max_value, max_index = stats.max(data)

    print(f"Min value for column {column_index}: {min_value:.2f} on day {min_index + 1}")
    print(f"Max value for column {column_index}: {max_value:.2f} on day {max_index + 1}")

    fp.close()

    # Compute thermocline for the min and max days
    print("\nComputing thermocline for min day:")
    compute_thermocline_for_day(min_index + 1, filename)

    print("\nComputing thermocline for max day:")
    compute_thermocline_for_day(max_index + 1, filename)

# Only execute main if this file is executed
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))

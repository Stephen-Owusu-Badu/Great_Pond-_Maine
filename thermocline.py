''''
thermocline.py

Stephen Owusu Badu
Fall 2024
CS152 Project 4

This program computes the thermocline depth for a specific day based on temperature data.
To run this program, type the following on the command line:
python3 thermocline.py <day>

Example:
python3 thermocline.py 5

'''

import stats
import sys

# Provided function to compute density from temperature
def compute_density_from_temp(temp):
    return 1000 * (1 - (temp + 288.9414) * (temp - 3.9863)**2 / (508929.2 * (temp + 68.12963)))

# Function to compute a list of densities from a list of temperatures
def compute_densities(temps):
    densities = []  # Create an empty list to store densities
    for temp in temps:
        # Convert each temperature to a density and append to densities list
        density = compute_density_from_temp(temp)
        densities.append(density)
    
    return densities  # Return the list of densities

# Function to compute the derivatives of the densities based on depth
def compute_density_derivatives(densities, depths):
    density_derivatives = []  # Create an empty list to store the derivatives
    for i in range(len(densities) - 1):
        # Compute the derivative for the current index
        density_derivative = (densities[i+1] - densities[i]) / (depths[i+1] - depths[i])
        # Append the computed derivative to the list
        density_derivatives.append(density_derivative)
    
    return density_derivatives  # Return the list of derivatives


# Function to compute the thermocline depth
def thermocline_depth(temps, depths):
    # Step 1: Compute densities from temperatures
    densities = compute_densities(temps)
    
    # Step 2: Compute density derivatives
    density_derivatives = compute_density_derivatives(densities, depths)
    
    # Step 3: Find the index of the maximum change in density
    max_derivative, max_index = stats.max(density_derivatives)
    
    # Step 4: Compute the thermocline depth
    # Use the mean of the depths at max_index and max_index + 1
    thermocline_depth = (depths[max_index] + depths[max_index + 1]) / 2
    
    # Step 5: Return the computed thermocline depth
    return thermocline_depth

def main(thermo_day):
    # Define depths where temperatures are measured and the corresponding column indices for those depths
    depths = [1, 3, 5, 7, 9, 11, 13, 15]
    depth_indices = [10, 11, 16, 17, 15, 14, 13, 12]

    # Open the data file
    fp = open("GoldieJulyNoon2019.csv", "r")

    # Read the headers (skip the first line)
    headers = fp.readline()

    # Initialize day counter
    day = 1

    # Loop through each line in the file
    for line in fp:
        # Check if we are on the second day
        if day == thermo_day:
            # Split the current line on commas to extract data
            items = line.split(',')

            # Initialize an empty list for temperatures
            temperatures = []

            # Loop over the depth indices to get corresponding temperatures
            for idx in depth_indices:
                # Append the temperature as a float
                temperatures.append(float(items[idx]))

            # Compute the thermocline depth using the temperatures and depths
            thermo_depth = thermocline_depth(temperatures, depths)

            # Print the thermocline depth in a readable format
            print(f"Thermocline depth for day {thermo_day} in July: {thermo_depth:.2f} meters")

        # Increment day counter for the next row
        day += 1

    # Close the file explicitly
    fp.close()

# Call the main function
if __name__ == "__main__":
    #main()

    print( sys.argv )


    ##file_name = sys.argv[ 2 ]

    thermo_day = int(sys.argv[1])  # Get the first command-line argument (day)
        
    #Call the main function and pass thermo_day
    main(thermo_day)
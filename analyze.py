'''
analyze.py

Stephen Owusu Badu
Fall 2024
CS152 Project 4

This script reads a CSV file and computes statistics (mean, min, max) for a specified data column. 
It prints the computed mean value, as well as the min and max values along with the day they occurred 
(based on their index in the dataset).

To run this program, type the following on the command line:
python3 analyze.py <filename> <column_index>

'''

# Add any imports here

# Add your functions up here

import stats
import sys

# main function
def main(filename, column_index):
    fp = open(filename, 'r')
    header = fp.readline().split(',')
    print(header)

    data = []
    for line in fp:
        items = line.split(',')
        data.append(float(items[column_index]))  # Assuming second column is at index 1
    print(data)
    

    
    mean = stats.compute_mean(data)
    print(mean)

# Compute the min and max using stats
    min_value, min_index = stats.min(data)
    max_value, max_index = stats.max(data)

    # Print min, max, and the corresponding days (index + 1)
    print(f"Min value for column {column_index}: {min_value:.2f} on day {min_index + 1}")
    print(f"Max value for column {column_index}: {max_value:.2f} on day {max_index + 1}")


    fp.close()
    #main(sys.argv[1], int(sys.argv[2]))
    #print(stats.compute_mean(data))


# only execute main if this file was executed
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))


    
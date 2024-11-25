# Ike Lage
# Spring 24
# CS 152 Project 4
#
# Test function for the density_derivatives function in the file thermocline.py
#
import thermocline

# computes densities for a set of temps and prints them out
def main():

    # some sample densities
    densities = [ 997. , 997.5 , 999. , 1000. ]

    # some sample depths
    depths = [ 2 , 4 , 6 , 8 ]

    density_derivatives = thermocline.compute_density_derivatives( densities , depths )

    # print out the derivatives
    print( density_derivatives )

    return

if __name__ == "__main__":
    main()
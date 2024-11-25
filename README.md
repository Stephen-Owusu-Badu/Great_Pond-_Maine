Thermocline Detection and Water Density Analysis in Great Pond, Maine

Abstract:  
This project explores the concept of thermoclines, a phenomenon in which temperature gradients in a body of water cause variations in density with depth. The goal is to analyze temperature data from Great Pond in the State of Maine and calculate the thermocline depth for specific days in July 2019. Using computational methods, I created Python functions to process CSV data, compute water densities, and identify the largest changes in density, which define the thermocline. Core computer science concepts such as modular design, file processing, and function implementation were essential in solving this problem. My key findings revealed significant temperature and density changes in July, with thermocline depths varying based on air temperature conditions.


Methods:  
To solve the problem of identifying thermocline depths, I used modular design principles. This involved breaking down the task into smaller, manageable functions, such as one to calculate water density from temperature and another to compute the derivative of density with respect to depth. A key computational strategy was iterating through the temperature data, calculating densities at each depth, and then using the `max` function to find the largest density change. This approach allowed me to automate the identification of the thermocline depth for any given day. Additionally, I had to handle noisy data by using smoothing techniques to ensure meaningful results.


"""
Program Name: Lab 15 - Plotting Cubic Numbers
Author: Xavier Chitison
Purpose: Generate and save graphs of the first 5 and first 5000 cubic numbers.
Starter Code: Based on the Chapter 15 Try It Yourself 15-1 assignment instructions.
Date: November 13, 2026
"""

import matplotlib.pyplot as plt


# Part 1: First 5 Cubes
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.plot(x_values, y_values, marker="o", color="blue")
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.grid(True)
plt.savefig("cubes_5.png")
plt.close()

# Part 2: First 5000 Cubes
x_values = list(range(1, 5001))
y_values = []

for number in x_values:
    y_values.append(number ** 3)

plt.plot(x_values, y_values, color="purple")
plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.grid(True)
plt.savefig("cubes_5000.png")
plt.close()
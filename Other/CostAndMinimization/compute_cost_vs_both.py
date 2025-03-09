'''
Compute the cost for various y-intercepts and slopes, and plot the cost vs. y-intercept and slope result
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Make data
x = np.array([2, 4, 6, 8, 10])                  # our GDP values
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])      # happiness values

# Model parameters/coefficients
intercepts = np.linspace(0, 2, 100)  # y-intercepts ranging from 0 to 2
slopes = np.linspace(0.25, 0.75, 100)  # slopes ranging from 1/4 to 3/4

# Create a meshgrid for intercepts and slopes
intercepts_grid, slopes_grid = np.meshgrid(intercepts, slopes)

# Initialize an array to hold the costs
costs = np.zeros(intercepts_grid.shape)

# Loop over intercepts and slopes and compute cost
for i in range(intercepts_grid.shape[0]):
    for j in range(intercepts_grid.shape[1]):
        intercept = intercepts_grid[i, j]
        slope = slopes_grid[i, j]
        modeldata = intercept + slope * x
        errors = data - modeldata
        cost = np.sum(errors**2)
        costs[i, j] = cost

# Plot cost vs. y-intercept and slope
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(intercepts_grid, slopes_grid, costs, cmap='viridis')

ax1.set_xlabel('Y-Intercept')
ax1.set_ylabel('Slope')
ax1.set_zlabel('Cost')
ax1.set_title('Cost vs. Y-Intercept and Slope')

plt.show()

# Plot log cost vs. y-intercept and slope
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
log_costs = np.log(costs)
ax2.plot_surface(intercepts_grid, slopes_grid, log_costs, cmap='viridis')

ax2.set_xlabel('Y-Intercept')
ax2.set_ylabel('Slope')
ax2.set_zlabel('Log(Cost)')
ax2.set_title('Log(Cost) vs. Y-Intercept and Slope')

plt.show()

# Find the index of the minimum cost
min_cost_index = np.argmin(costs)
min_cost_intercept = intercepts_grid.flatten()[min_cost_index]
min_cost_slope = slopes_grid.flatten()[min_cost_index]
min_cost = costs.flatten()[min_cost_index]

print(f"The minimum cost is {min_cost}")
print(f"The y-intercept for the minimum cost is {min_cost_intercept}")
print(f"The slope for the minimum cost is {min_cost_slope}")
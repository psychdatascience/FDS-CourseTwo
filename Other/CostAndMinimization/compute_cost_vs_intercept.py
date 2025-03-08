'''
Compute the cost for various y-intercepts and plot the cost vs. y-intercept result
'''

import numpy as np
import matplotlib.pyplot as plt

# Make data
x = np.array([2, 4, 6, 8, 10])                  # x values
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])      # data values

# Model parameters/coefficients
slope = 0.5
intercepts = np.linspace(0, 2, 100)  # y-intercepts ranging from 0 to 2

costs = []

# Loop over intercepts and compute cost
for intercept in intercepts:
    modeldata = intercept + slope * x
    errors = data - modeldata
    cost = np.sum(errors**2)
    costs.append(cost)

# Plot cost vs. y-intercept
plt.plot(intercepts, costs, 'b-')
plt.xlabel('Y-Intercept')
plt.ylabel('Cost')
plt.title('Cost vs. Y-Intercept')
plt.show()
'''
Compute the cost for various y-intercepts and plot the cost vs. y-intercept result
'''

import numpy as np
import matplotlib.pyplot as plt

# Make data
x = np.array([2, 4, 6, 8, 10])                  # our GDP values
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])      # happiness values

# Model parameters/coefficients
slope = 0.5 # slope is fixed at 0.5 - we are only varying the y-intercept
intercepts = np.linspace(0, 2, 100)  # y-intercepts ranging from 0 to 2

costs = [] # to hold costs for our various y-intercepts

# Loop over intercepts and compute cost 
for intercept in intercepts:           # loop over y-intercepts
    modeldata = intercept + slope * x  # compute model data
    errors = data - modeldata          # compute errors
    cost = np.sum(errors**2)           # compute cost
    costs.append(cost)                 # store cost for this y-intercept

# Plot cost vs. y-intercept
plt.plot(intercepts, costs, 'b-o')
plt.xlabel('Y-Intercept')
plt.ylabel('Cost')
plt.title('Cost vs. Y-Intercept')
plt.show()

print(f'the minimum cost is {np.min(costs)}')
print(f'the y-intercept for the minimum cost is {intercepts[np.argmin(costs)]}')


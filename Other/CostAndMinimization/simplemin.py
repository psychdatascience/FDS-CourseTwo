'''
Simple example of computing a model, errors, and cost
Linear-ish data, linear model, fit the y-intercept only!
'''

import numpy as np


## Make data
x = np.array([2, 4, 6, 8, 10])                  # x values
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])      # data values

# plot the data values
# plt.plot(x, data, 'ro')
# plt.show()


## Make model
modeldata = np.zeros(data.shape)                # array to hold model data values

# Model parameters/coefficients
b_intercept = 0
b_slope = 0.5

# Compute model values
for index, x_in in enumerate(x) :
    y_out = b_intercept + b_slope*x_in
    modeldata[index] = y_out

## Compute cost (total error)
# compute individual errors
errors = data - modeldata

# compute cost
cost = 0
for cost in errors :
    cost += cost

# And we're done!

print(f"data: {data}")
print(f"model data: {modeldata}")
print(f"errors: {errors}")
print(f"cost is {cost}")


'''
Simple example of computing a model, errors, and cost
Linear-ish data, linear model, fit the y-intercept only!
'''

import numpy as np
import matplotlib.pyplot as plt

# Make data
x = np.array([2, 4, 6, 8, 10])                  # x values
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])      # data values

# plot the data values
plt.plot(x, data, 'ro')
plt.xlabel('Nation\'s GDP')
plt.ylabel('Nation\'s Happiness')
plt.title('Nation\'s Happiness vs GDP')
plt.show()

## Make model
modeldata = np.zeros(data.shape)                # array to hold model data values

# Model parameters/coefficients
intercept = 0
slope = 0.5

# Compute model values
for index, x_in in enumerate(x) :
    y_out = intercept + slope*x_in
    modeldata[index] = y_out

# plot the model values on the same plot as the data
plt.plot(x, data, 'ro')         # data
plt.plot(x, modeldata, 'b-')    # model
plt.legend(['data', 'model'])
plt.show()

# plot the model values and errors on the same plot as the data
plt.plot(x, data, 'ro')         # data
plt.plot(x, modeldata, 'b-')    # model

# Add vertical lines to represent errors
for i in range(len(x)):
    plt.vlines(x[i], modeldata[i], data[i], colors='g', linestyles='dashed')

plt.show()
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


import numpy as np

## Make data
x = np.array([2, 4, 6, 8, 10])
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])
modeldata = np.zeros(data.shape)

## Make model
# Model parameters/coefficients
b_intercept = 0
b_slope = 0.5

# Model formula: y_out = b_intercept + b_slope*x_in

for index, x_in in enumerate(x) :
    y_out = b_intercept + b_slope*x_in
    modeldata[index] = y_out

print(modeldata)

## Compute errors and cost (total error)
errors = data - modeldata
cost = 0
for cost in errors :
    cost += cost

print(f"cost is {cost}")


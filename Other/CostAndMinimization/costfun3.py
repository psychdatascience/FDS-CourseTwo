
'''
costfun3:
Expanding costmin2.py to do a slightly-less primitive minimization crossing over the min
Each time we cross the min (cost begins to increase), we'll reverse direction and reduce the step size
Compute direction of error, step..., reverse, smaller step..., terminate
fit the y-intercept only!
'''

import numpy as np
import matplotlib.pyplot as plt

## Make data
x = np.array([2, 4, 6, 8, 10])
data = np.array([1.8, 3.3, 3.7, 4.6, 6.7])
modeldata = np.zeros(data.shape)

## Make model
# Model parameters/coefficients
b_slope = 0.5
b_intercept = 0
delta_intercept = 0.25    # amount we're going to change the vertical offset (intercept)

### Here's the (first?) loop to minimize cost function
## Loop until sign flips

# set up vars for while loop
# python lists for candidate intercept and cost value (total error) so we can append
hypoth_intercepts = []
costs = []
while_index = 0           # to keep track of how many steps we took

cost = 1000               # just so we jump into the while loop
print("entering first while")
while cost > 0 :
    for index, x_in in enumerate(x) :
        y_out = b_intercept + b_slope*x_in          # y-intercept the thing we're changing
        modeldata[index] = y_out
    
    ## Compute errors and cost (total error)
    errors = data - modeldata
    cost = 0
    for cost in errors :
        cost += cost
    
    # Store the intercept and cost values
    hypoth_intercepts.append(b_intercept)
    costs.append(cost)
    
    # update the y-intercept and the while loop number
    b_intercept += delta_intercept
    while_index += 1

print("out of first while")

## now let's try to come at the min from the other direction!
b_intercept = 4           # Come at the min from the other side, model line way above the data
while_index = 0           # to keep track of how many steps we took
cost = 1000                  # just so we jump into the while loop
print("entering second while")
while cost > 0.42 :          # This time, we'll start below a cost theshold 
    for index, x_in in enumerate(x) :
        y_out = b_intercept + b_slope*x_in          # y-intercept the thing we're changing
        modeldata[index] = y_out
    
    ## Compute errors and cost (total error)
    errors = data - modeldata
    cost = 0
    for cost in errors :
        cost = abs(cost)
        cost += cost                                 # uh oh! Cost can go negative! We need a new threshold!!
    
    # Store the intercept and cost values
    hypoth_intercepts.append(b_intercept)
    costs.append(cost)
    
    # update the y-intercept and the while loop number
    b_intercept -= delta_intercept
    while_index += 1

print("out of second while")

print(f"data: {data}")
print(f"model data: {modeldata}")
print(f"errors: {errors}")
print(f"cost is {cost}")
print(f"final best fit intercept is {b_intercept} after {while_index + 1} iterations")

print(f"model intercepts: {hypoth_intercepts}")
print(f"costs: {costs}")

### Plotting
plt.plot(hypoth_intercepts, costs, 'o-r')
plt.xlabel("y intercept of line")
plt.ylabel("Cost (SE)")
plt.show()


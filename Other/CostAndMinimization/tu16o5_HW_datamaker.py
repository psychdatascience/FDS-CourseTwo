'''
This script generates a dataset for the homework problem in tu16o5_HW.py
'''     

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

X_LIM = 10
MEAN = 0
STD = 2
N = 42

x = np.linspace(-X_LIM, X_LIM, N)
y = 2*x + STD*np.random.randn(x.size) + MEAN

plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data for Homework Problem')
plt.show()  

to_save = input('Save data to tu16o5_HW_data.csv? (y/n): ')
if to_save != 'y':
    print('Data not saved')
    exit()

# Convert to DataFrame
df = pd.DataFrame({'x': x, 'y': y}) 
df.to_csv('tu16o5_HW_data.csv', index=False)
print('Data saved to tu16o5_HW_data.csv')


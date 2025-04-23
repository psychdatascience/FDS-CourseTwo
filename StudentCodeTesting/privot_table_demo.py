'''
Demonstration of pivot table
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Constants, etc.
n_signs = 3
n_players = 4
sign = ['tiger', 'dragon', 'snake']

# Create a list of WR signs
wr_sign = n_signs * sign
# print(wr_sign)

# Create a list of QB signs
qb_sign = []
for temp in sign:
    for _ in range(n_signs):
        qb_sign.append(temp)
# print(qb_sign)

# make complete lists for the dataframe
wr_sign = wr_sign * n_players
qb_sign = qb_sign * n_players

# create random yards data for each player combination
yards = np.random.randint(1, 100, n_signs * len(sign) * n_players)
# print(yards)

# Create the DataFrame
df = pd.DataFrame({
    'wr_sign': wr_sign,
    'qb_sign': qb_sign,
    'yards': yards
})
print(df)

# Create a pivot table
pivot_table = df.pivot_table(index='wr_sign', columns='qb_sign', values='yards', aggfunc='sum')
print(pivot_table)

# Plot the pivot table
#plt.figure(figsize=(11, 8))
sns.heatmap(pivot_table, annot=True, fmt='d', cmap='coolwarm', 
           linewidths=.5, cbar_kws={"shrink": .8},
           vmin=0, vmax=400)
plt.title('Pivot Table Heatmap')
plt.xlabel('QB Sign')
plt.ylabel('WR Sign')
plt.show()
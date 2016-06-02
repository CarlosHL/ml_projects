import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import cleaningData

# data
x, y = cleaningData.CleanData('ex1data1.txt').clean_data()

fig, ax = plt.subplots()
ax.scatter(x,y,color='blue',s=5,edgecolor='none')
ax.set_aspect(1./ax.get_data_ratio()) # make axes square

print "> Plotting data"
fig.suptitle('Population-Profit Graph', fontsize=20)
plt.xlabel('Population of city in 10.000s', fontsize=16)
plt.ylabel('Profit in $10.000', fontsize=16)
fig.savefig('graph1.png')

#plt.show()

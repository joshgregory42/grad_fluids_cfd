import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.sans-serif": ["Computer Modern Roman"]})

data_2020 = pd.read_csv('force_plot_2020.csv')
data_2022 = pd.read_csv('force_plot_2022.csv')

y_force_20 = data_2020['TOTAL_FORCE_Y']
y_force_22 = data_2022['TOTAL_FORCE_Y']



plt.plot(abs(y_force_20), 'r', linewidth=0.5, label='Old Wing')
plt.plot(abs(y_force_22), 'b', linewidth=0.5, label='New Wing')
plt.xlabel('Time step')
plt.ylabel('Force (N)')
plt.grid(axis='y')
plt.legend(loc='best')
plt.savefig('y_force_compare.png', dpi=1000)
plt.show()

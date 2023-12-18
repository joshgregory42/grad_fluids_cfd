import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Read first and third columns from new_data.xlsx
new_data_df = pd.read_excel('new_wing_data.xlsx', usecols=[0, 2])

# Read first and third columns from old_data.xlsx
old_data_df = pd.read_excel('old_wing_data.xlsx', usecols=[0, 2])

new_downforce = np.abs(new_data_df[new_data_df.columns[1]])

old_downforce = np.abs(old_data_df[old_data_df.columns[1]])

delta = pd.DataFrame(new_downforce - old_downforce)

# Running statistical t-test
t_statistic, p_value = stats.ttest_ind(new_downforce, old_downforce, equal_var=False)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# Plot new_data_df
plt.figure()
plt.plot(old_data_df[old_data_df.columns[0]], np.abs(old_data_df[old_data_df.columns[1]]), label='Old wing', color='r', linestyle=':')
plt.plot(new_data_df[new_data_df.columns[0]], np.abs(new_data_df[new_data_df.columns[1]]), label='New wing', color='b')
plt.xlabel('Air speed (m/s)')
plt.ylabel('Downforce (N)')
plt.grid(True)
plt.legend()
plt.show()


# Write new_data_df to a CSV file
new_data_df.to_csv('new_data_df.csv', index=False)

# Write old_data_df to a CSV file
old_data_df.to_csv('old_data_df.csv', index=False)

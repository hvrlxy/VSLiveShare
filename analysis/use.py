import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy import stats

# initialize a pandas data frame with column ID, USEFULNESS, EASE OF USE, EASE OF LEARNING, SATISFACTION, and group
df = pd.DataFrame({'ID': [1, 2, 3, 4, 5, 6, 7, 8], 'USEFULNESS': [35, 39, 30, 44, 56, 56, 56, 40], 
                     'EASE OF USE': [63, 61, 50, 71, 70, 70, 70, 50],
                        'EASE OF LEARNING': [25, 24, 20, 27, 28, 28, 28, 20],
                            'SATISFACTION': [34, 38, 31, 49, 49, 49, 49, 40],
                                'group': ['INTERVENTION', 'INTERVENTION', 'INTERVENTION', 'INTERVENTION', 'CONTROL', 'CONTROL', 'CONTROL', 'CONTROL']})

# print out the t-test results for the intervention group and the control group for each column
# print(stats.ttest_ind(df[df['group'] == 'INTERVENTION']['USEFULNESS'], df[df['group'] == 'CONTROL']['USEFULNESS']))
# print(stats.ttest_ind(df[df['group'] == 'INTERVENTION']['EASE OF USE'], df[df['group'] == 'CONTROL']['EASE OF USE']))
# print(stats.ttest_ind(df[df['group'] == 'INTERVENTION']['EASE OF LEARNING'], df[df['group'] == 'CONTROL']['EASE OF LEARNING']))
# print(stats.ttest_ind(df[df['group'] == 'INTERVENTION']['SATISFACTION'], df[df['group'] == 'CONTROL']['SATISFACTION']))
# # plot a violin plot of usefulness by group
# sns.violinplot(x='group', y='EASE OF LEARNING', data=df)
# # add title
# plt.title('EASE OF LEARNING by Group')
# # add x and y labels
# # plt.xlabel('Group')
# plt.ylabel('EASE OF LEARNING (out of 28)')
# # save the plot
# plt.show()

# plot the histogram for EASE OF USE
sns.displot(df['EASE OF LEARNING'])
# change the bin size to 10
plt.xticks(np.arange(df['EASE OF LEARNING'].min(), df['EASE OF LEARNING'].max(), 5))
# add title
plt.title('EASE OF LEARNING Distribution')
# add x and y labels
plt.xlabel('EASE OF LEARNING (out of 56)')
plt.ylabel('Frequency')
# show legend
plt.legend()
# show plot
plt.show()

#calculate mean and standard deviation for each group
print(df[df['group'] == 'INTERVENTION']['EASE OF LEARNING'].mean())
print(df[df['group'] == 'INTERVENTION']['EASE OF LEARNING'].std())
print(df[df['group'] == 'CONTROL']['EASE OF LEARNING'].mean())
print(df[df['group'] == 'CONTROL']['EASE OF LEARNING'].std())



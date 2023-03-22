import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy import stats

# initialize a pandas data frame with groupID, score, and group
df = pd.DataFrame({'groupID': [1, 2, 3, 4], 'pylint score': [1.53, 1.015, 0.0, 3.165],
                        'group': ['INTERVENTION', 'INTERVENTION', 'CONTROL', 'CONTROL']})

# create a boxplot of score by group
# sns.boxplot(x='group', y='pylint score', data=df)
# # add title
# plt.title('Pylint Score by Group')
# # add x and y labels
# plt.xlabel('Group')
# plt.ylabel('Pylint Score')
# #show legend
# plt.legend()
# # show plot
# plt.show()

# perform a t-test print out the results
# ttest = stats.ttest_ind(df[df['group']=='INTERVENTION']['pylint score'], df[df['group']=='CONTROL']['pylint score'])
# print(ttest)

# create a histogram for the score
# sns.distplot(df['pylint score'])
# # add title
# plt.title('Pylint Score Distribution')
# # add x and y labels
# plt.xlabel('Pylint Score')
# plt.ylabel('Frequency')
# # show plot
# plt.show()

# print the mean and standard deviation for each group
# print(df[df['group'] == 'INTERVENTION']['pylint score'].mean())
# print(df[df['group'] == 'INTERVENTION']['pylint score'].std())
# print(df[df['group'] == 'CONTROL']['pylint score'].mean())
# print(df[df['group'] == 'CONTROL']['pylint score'].std())
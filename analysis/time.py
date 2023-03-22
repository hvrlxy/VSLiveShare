# import pandas, numpy, matplotlib, seaborn, scipy, statsmodels, sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy import stats

# initialize a pandas data frame with column groupID, time, and group
df = pd.DataFrame({'groupID': [1, 2, 3, 4], 'time': [23, 46, 25, 26], 
                   'group': ['INTERVENTION', 'INTERVENTION', 'CONTROL', 'CONTROL']})

# plot a boxplot of time by group
sns.boxplot(x='group', y='time', data=df)
# add title
plt.title('Completion Time by Group')
# add x and y labels
# plt.xlabel('Group')
plt.ylabel('Completion Time (minutes)')

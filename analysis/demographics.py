import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy import stats

# read the data into a pandas data frame
df = pd.read_csv('/Users/hale/Desktop/VSLiveShare/results/Investigating the Efficiency and Usefulness of VSCode LiveShare in Assisting Remote Collaboration (Responses) - Form Responses 1.csv')

#remove Timestamp and Email Address columns
df = df.drop(['Timestamp', 'Email Address', 'Do you have any thoughts on the pair programming session?',
       'How familiar are you with code live sharing platforms?',
       'How familiar are you with LeetCode and similar coding challenge platforms?'], axis=1)

#rename columns into Age, Gender, Experience, and Education
df.columns = ['Age', 'Gender', 'Experience', 'Education']
# remove substring  (4-year degree) from Education column
df['Education'] = df['Education'].str.replace(' \(4-year degree\)', '')
#remove the first row
df = df.drop([0], axis=0)
print(df)

# create a pie chart to show the distribution of Age
df['Education'].value_counts().plot(kind='pie', autopct='%1.0f%%')
#make the title bold
plt.title('Hishest Education Distribution', fontweight='bold')
# remove the y label
plt.ylabel('')
# show plot
plt.show()
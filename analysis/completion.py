import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy import stats

# initialize a pandas data frame with groupID, completion rate, and group
df = pd.DataFrame({'groupID': [1, 2, 3, 4], 'completion rate': [1.0, 1.0, 0.5, ],
                        'group': ['INTERVENTION', 'INTERVENTION', 'CONTROL', 'CONTROL']})
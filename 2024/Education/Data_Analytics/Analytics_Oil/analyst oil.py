import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib

df = pd.read_csv('brent-monthly.csv')

plt.plot('Date', 'Price', data=df, color='tab:red')
plt.show()

sns.set_style("darkgrid")
sns.lineplot(data=df, x='Date', y='Price')
plt.show()
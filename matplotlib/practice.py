import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv(r"/Users/praneelchetlapalli/Downloads/deliveries.csv")
sns.boxplot(x="over",y="total_runs",data=df)
plt.title("overs vs runs")
plt.xlabel("runs")
plt.ylabel("over")
plt.show()
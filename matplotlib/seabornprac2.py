import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
# # Update with the correct path if needed
df = pd.read_csv(r"/Users/praneelchetlapalli/Downloads/deliveries.csv")

# 1. Run Distribution Per Over
plt.figure(figsize=(10, 6))
sns.boxplot(x='over', y='total_runs', data=df)
plt.xlabel('Over')
plt.ylabel('Total Runs')
plt.title('Run Distribution Per Over')

# 2. Most Successful Batters
top_batters = df.groupby('batter')['batsman_runs'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
top_batters.plot(kind='bar', color='skyblue')
plt.xlabel('Batter')
plt.ylabel('Total Runs')
plt.title('Top 10 Batters with Highest Total Runs')
plt.xticks(rotation=45)

# 3. Extras Analysis
plt.figure(figsize=(10, 6))
sns.countplot(y='extras_type', data=df, order=df['extras_type'].value_counts().index, palette='viridis')
plt.xlabel('Count')
plt.ylabel('Extras Type')
plt.title('Frequency of Different Extra Types')

# 4. Wicket Analysis
dismissals = df['dismissal_kind'].dropna().value_counts()
plt.figure(figsize=(8, 8))
plt.pie(dismissals, labels=dismissals.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Proportion of Different Modes of Dismissal')

# 5. Bowler Economy Rate
bowler_stats = df.groupby('bowler').agg({'total_runs': 'sum', 'over': 'count'})
bowler_stats['economy_rate'] = bowler_stats['total_runs'] / (bowler_stats['over'] / 6)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=bowler_stats['over'], y=bowler_stats['economy_rate'], alpha=0.6)
plt.xlabel('Overs Bowled')
plt.ylabel('Economy Rate')
plt.title('Bowler Economy Rate vs Overs Bowled')
plt.show()

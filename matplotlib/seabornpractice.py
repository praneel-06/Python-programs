import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv(r"/Users/praneelchetlapalli/Downloads/cereal.csv")
plt.figure(figsize=(12, 6))
nutritional_cols = ['Calories', 'Protein (g)', 'Fat', 'Sodium', 'Dietary Fiber', 'Carbs', 'Sugars', 'Potassium']
sns.boxplot(data=df[nutritional_cols])
plt.title("Distribution of nutrional attributes ")
plt.xlabel("Nutrional attributes")
plt.ylabel("values")
plt.show()
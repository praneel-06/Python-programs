import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
# Update with the correct path if needed
df_cereal = pd.read_csv(r"/Users/praneelchetlapalli/Downloads/cereal.csv")

# Create a figure with subplots
fig, axes = plt.subplots(3, 2, figsize=(14, 10))

# (a) Boxplots & Histograms for Nutritional Statistics
nutritional_cols = ['Calories', 'Protein (g)', 'Fat', 'Sodium', 'Dietary Fiber', 'Carbs', 'Sugars', 'Potassium']

# Boxplots
axes[0, 0].boxplot([df_cereal[col].dropna() for col in nutritional_cols], vert=False, patch_artist=True)
axes[0, 0].set_yticklabels(nutritional_cols)
axes[0, 0].set_title("Boxplots of Nutritional Attributes")
axes[0, 0].set_xlabel("Value")

# Histogram for Sugar content
axes[0, 1].hist(df_cereal['Sugars'].dropna(), bins=10, color='blue', edgecolor='black', alpha=0.5)
axes[0, 1].set_title("Histogram of Sugar Content")
axes[0, 1].set_xlabel("Sugar Content (g)")
axes[0, 1].set_ylabel("Frequency")

# (b) Bar Chart & Scatter Plot for Cereal Ratings
df_cereal_sorted = df_cereal.sort_values(by='Sugars')  # Sorting for visualization

# Bar Chart for Ratings
axes[1, 0].barh(df_cereal_sorted['Cereal Name'][:10], df_cereal_sorted['Sugars'][:10], color='orange', alpha=0.7)
axes[1, 0].set_title("Cereals with Lowest Sugar Content")
axes[1, 0].set_xlabel("Sugar Content (g)")
axes[1, 0].set_ylabel("Cereal Name")

# Scatter Plot of Sugar vs Rating
axes[1, 1].scatter(df_cereal['Sugars'], df_cereal['Vitamins and Minerals'], color='red', alpha=0.7)
axes[1, 1].set_title("Sugar Content vs Cereal Ratings")
axes[1, 1].set_xlabel("Sugar Content (g)")
axes[1, 1].set_ylabel("Ratings")

# Adjust layout
##plt.tight_layout()
##plt.show()
##
### Additional visualizations for (c) and (d)
##fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# (c) Scatter Plot with Regression Line (Sugar vs Ratings)
x = df_cereal['Sugars']
y = df_cereal['Vitamins and Minerals']

# Scatter plot
axes[2,0].scatter(x, y, color='purple', alpha=0.7, label='Data Points')

# Regression line (Least Squares Fit)
m, b = np.polyfit(x, y, 1)
axes[2,0].plot(x, m*x + b, color='black', linestyle='dashed', label='Trend Line')

axes[2,0].set_title("Correlation: Sugar Content vs Cereal Ratings")
axes[2,0].set_xlabel("Sugar Content (g)")
axes[2,0].set_ylabel("Ratings")
axes[2,0].legend()

# (d) Boxplot for Ratings by Manufacturer
manufacturers = df_cereal['Manufacturer'].unique()
data = [df_cereal[df_cereal['Manufacturer'] == manu]['Vitamins and Minerals'].dropna() for manu in manufacturers]

# Boxplot
axes[2,1].boxplot(data, labels=manufacturers, patch_artist=True)
axes[2,1].set_title("Cereal Ratings by Manufacturer")
axes[2,1].set_xlabel("Manufacturer")
axes[2,1].set_ylabel("Ratings")

# Show the plots
plt.tight_layout()
plt.show()

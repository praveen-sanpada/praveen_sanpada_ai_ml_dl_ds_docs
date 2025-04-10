# ✅ visualization_essentials.py – Matplotlib & Seaborn Full Guide

# visualization_essentials.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}
df = pd.DataFrame(data)

tips = sns.load_dataset('tips')  # Built-in Seaborn dataset

# --------------------------------------------
# ✅ 1. Basic Plotting with Matplotlib
# --------------------------------------------

# Line plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()

# Bar chart
plt.bar(df['Category'], df['Values'], color='orange')
plt.title("Bar Chart")
plt.ylabel("Values")
plt.show()

# Horizontal bar chart
plt.barh(df['Category'], df['Values'], color='purple')
plt.title("Horizontal Bar Chart")
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='green')
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Pie chart
sizes = [40, 30, 20, 10]
labels = ['Apple', 'Banana', 'Cherry', 'Date']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("Pie Chart")
plt.show()

# Box plot
plt.boxplot([np.random.randn(100), np.random.randn(100) + 1])
plt.title("Box Plot")
plt.show()

# ------------------------------------------------------
# ✅ 2. Seaborn Basics (Stylish & Statistical Visuals)
# ------------------------------------------------------

# Histogram using Seaborn
sns.histplot(tips['total_bill'], bins=30, kde=True, color='skyblue')
plt.title("Total Bill Distribution")
plt.show()

# Boxplot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title("Boxplot of Total Bill by Day")
plt.show()

# Violin plot
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title("Violin Plot of Total Bill by Day")
plt.show()

# Count plot (like bar plot for categorical data)
sns.countplot(x='day', data=tips)
plt.title("Count of Meals by Day")
plt.show()

# Bar plot (statistical bar)
sns.barplot(x='day', y='total_bill', data=tips, estimator=np.mean)
plt.title("Average Total Bill by Day")
plt.show()

# Scatter plot with regression line
sns.regplot(x='total_bill', y='tip', data=tips)
plt.title("Regression: Tip vs Total Bill")
plt.show()

# Pair plot (scatter matrix)
sns.pairplot(tips)
plt.suptitle("Pair Plot of Tips Dataset", y=1.02)
plt.show()

# Heatmap (correlation matrix)
correlation = tips.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# --------------------------------------------
# ✅ 3. Customizing Plots
# --------------------------------------------

# Multiple subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot([1, 2, 3], [4, 5, 6])
axs[0].set_title("Plot 1")

axs[1].bar(['A', 'B', 'C'], [10, 20, 15])
axs[1].set_title("Plot 2")

plt.suptitle("Multiple Subplots")
plt.tight_layout()
plt.show()

# Change figure size
plt.figure(figsize=(8, 5))
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Custom Size Plot")
plt.show()

# Save plot to file
plt.plot([1, 2, 3], [3, 2, 1])
plt.title("Save This Plot")
plt.savefig("my_plot.png")
plt.show()


# =================================================================================================

# ✅ Summary – All Essential Functions (With Examples)
# Feature	Matplotlib	Seaborn
# Line Plot	plt.plot()	sns.lineplot() (optional)
# Bar Chart	plt.bar()	sns.barplot()
# Horizontal Bar	plt.barh()	—
# Scatter Plot	plt.scatter()	sns.scatterplot() / regplot()
# Histogram	plt.hist()	sns.histplot()
# Pie Chart	plt.pie()	—
# Box Plot	plt.boxplot()	sns.boxplot()
# Violin Plot	—	sns.violinplot()
# Count Plot (Categories)	—	sns.countplot()
# Regression Plot	—	sns.regplot()
# Pair Plot	—	sns.pairplot()
# Heatmap (correlation)	—	sns.heatmap()
# Subplots	plt.subplots()	—
# Titles & Labels	plt.title(), plt.xlabel()	plt.title()
# Save Figure	plt.savefig('file.png')	—

# ✅ Real-World Use Case:
# Use Matplotlib and Seaborn to:
# Create EDA reports
# Visualize trends, comparisons, and correlations
# Enhance data storytelling for dashboards and ML projects

# =================================================================================================

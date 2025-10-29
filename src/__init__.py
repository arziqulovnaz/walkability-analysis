import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load mock dataset
df = pd.read_csv('data/walkability_scores.csv')
df.head()

df['combined_score'] = (
    0.6 * df['walk_score'] + 
    0.4 * df['distance_to_transit']
)

corr = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
plt.imshow(corr, cmap='coolwarm', interpolation='none')
plt.colorbar(label='Correlation')
plt.xticks(range(len(corr)), corr.columns, rotation=45, ha='right')
plt.yticks(range(len(corr)), corr.columns)
plt.title('Feature Correlation Heatmap')
plt.show()


# Top 10 most walkable areas
top_walkable = df.sort_values('walk_score', ascending=False).head(10)
print("Top 10 Walkable Areas:")
display(top_walkable[['suburb', 'walk_score', 'distance_to_transit', 'combined_score']])

# Bottom 10 least walkable
bottom_walkable = df.sort_values('walk_score').head(10)
print("\nBottom 10 Walkable Areas:")
display(bottom_walkable[['suburb', 'walk_score', 'distance_to_transit', 'combined_score']])

# Visualize relationship between walkability & livability

plt.figure(figsize=(8,6))
plt.scatter(df['walk_score'], df['livability_index'], alpha=0.7)
plt.title('Walkability vs Livability')
plt.xlabel('Walk Score')
plt.ylabel('Livability Index')
plt.grid(True)
plt.show()

# Compare public transport vs walk score

plt.figure(figsize=(8,6))
plt.scatter(df['distance_to_transit'], df['walk_score'], alpha=0.7)
plt.title('Public Transport Access vs Walkability')
plt.xlabel('Public Transport Access')
plt.ylabel('Walk Score')
plt.grid(True)
plt.show()

# Cluster analysis

features = df[['walk_score', 'livability_index', 'distance_to_transit']]
scaled = StandardScaler().fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(scaled)

df.groupby('cluster')[['walk_score', 'livability_index', 'distance_to_transit']].mean()

# Visualization of clusters

plt.figure(figsize=(8,6))
plt.scatter(df['walk_score'], df['livability_index'], c=df['cluster'], cmap='viridis', alpha=0.7)
plt.title('Clustered Walkability-Livability Profiles')
plt.xlabel('Walk Score')
plt.ylabel('Livability Index')
plt.grid(True)
plt.show()

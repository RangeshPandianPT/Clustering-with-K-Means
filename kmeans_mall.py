
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Mall_Customers.csv")
df_clean = df.select_dtypes(include=["number"]).dropna()

pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_clean)
df_pca = pd.DataFrame(pca_result, columns=["PCA1", "PCA2"])

inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_clean)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.title("Elbow Method")
plt.xlabel("K")
plt.ylabel("Inertia")
plt.savefig("mall_elbow_curve.png")
plt.close()

kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(df_clean)
df_pca["Cluster"] = labels

sns.scatterplot(x="PCA1", y="PCA2", hue="Cluster", data=df_pca, palette="Set2")
plt.title("K-Means Clustering")
plt.savefig("mall_cluster_visualization.png")
plt.close()

score = silhouette_score(df_clean, labels)
print("Silhouette Score:", score)

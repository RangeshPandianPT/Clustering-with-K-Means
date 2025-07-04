This project applies **K-Means Clustering** on the popular **Mall Customer Segmentation** dataset to group customers into distinct clusters based on their spending behavior and demographics.

## 📁 Files Included

- `Mall_Customers.csv` — Dataset used for clustering  
- `kmeans_mall.py` — Python script for clustering and visualization  
- `kmeans_mall.ipynb` — Jupyter Notebook version for interactive exploration  
- `mall_elbow_curve.png` — Elbow method plot to determine optimal number of clusters  
- `mall_cluster_visualization.png` — 2D PCA cluster visualization  

## 🧪 Project Workflow

1. **Data Loading & Cleaning**  
   Only numerical features are selected for clustering.

2. **Dimensionality Reduction (PCA)**  
   PCA is applied to project data into 2D for visualization purposes.

3. **K-Means Clustering**  
   - The Elbow Method is used to find the optimal number of clusters (K).
   - K-Means is then fitted on the data.
   - Cluster labels are assigned to each customer.
  
   ---

4. **Visualization**
 
![Image](https://github.com/user-attachments/assets/94a3ccb4-1212-43d7-9bdf-234334b61318)

![Image](https://github.com/user-attachments/assets/e79c2755-2f3b-4035-be77-bd02de8a7bb5)

---

5. **Evaluation**  
   - **Silhouette Score** is used to evaluate clustering quality.

## 📊 Silhouette Score

The clustering model achieved a silhouette score of approximately `0.xx` (printed during execution), indicating the quality of the clustering.

## 📚 Requirements

- Python 3.x  
- `pandas`, `matplotlib`, `seaborn`, `scikit-learn`

Install dependencies using:

```bash
pip install pandas matplotlib seaborn scikit-learn
````

## 📌 Dataset Source

This dataset is commonly used in clustering problems and contains customer details like Age, Annual Income, and Spending Score.

## ✅ Use Cases

* Customer segmentation for targeted marketing
* Behavioral clustering
* Retail strategy optimization

---

### 💡 Author

RANGESHPANDIAN PT




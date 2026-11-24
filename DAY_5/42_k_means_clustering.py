# 42 K-Means clustering
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
X=StandardScaler().fit_transform(load_iris().data)
m=KMeans(n_clusters=3,random_state=42,n_init=10).fit(X)
print("Labels",m.labels_,"Silhouette",silhouette_score(X,m.labels_))
# 39 Principal component analysis
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
X=StandardScaler().fit_transform(load_iris().data)
p=PCA(n_components=2);Z=p.fit_transform(X)
print("Original",X.shape,"Reduced",Z.shape,"Variance",p.explained_variance_ratio_)
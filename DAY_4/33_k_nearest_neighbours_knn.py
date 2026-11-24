# 33 KNN classifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
d=load_iris();a,b,c,e=train_test_split(d.data,d.target,test_size=.2,random_state=42)
m=KNeighborsClassifier(n_neighbors=5).fit(a,c);print("Accuracy",accuracy_score(e,m.predict(b)))
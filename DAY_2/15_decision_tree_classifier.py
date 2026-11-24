# 15 Decision tree on Iris
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
d=load_iris();X,x,y,Y=train_test_split(d.data,d.target,test_size=.25,random_state=42)
m=DecisionTreeClassifier(max_depth=3).fit(X,y);print(accuracy_score(Y,m.predict(x)))
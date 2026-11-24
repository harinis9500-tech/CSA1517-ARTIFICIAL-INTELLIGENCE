# 35 Decision tree classification
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
d=load_breast_cancer();a,b,c,e=train_test_split(d.data,d.target,test_size=.25,random_state=7)
m=DecisionTreeClassifier(max_depth=4).fit(a,c);print(classification_report(e,m.predict(b)))
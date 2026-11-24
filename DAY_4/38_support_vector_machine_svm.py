# 38 Support vector machine
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
d=load_breast_cancer();a,b,c,e=train_test_split(d.data,d.target,test_size=.25,random_state=42)
m=make_pipeline(StandardScaler(),SVC()).fit(a,c);print("Accuracy",m.score(b,e))
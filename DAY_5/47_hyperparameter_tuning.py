# 47 Hyperparameter tuning with GridSearchCV
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
d=load_iris();a,b,c,e=train_test_split(d.data,d.target,test_size=.2,random_state=42)
g=GridSearchCV(RandomForestClassifier(random_state=1),{"n_estimators":[50,100],"max_depth":[None,3,5]},cv=5)
g.fit(a,c);print("Best parameters",g.best_params_,"Test score",g.score(b,e))
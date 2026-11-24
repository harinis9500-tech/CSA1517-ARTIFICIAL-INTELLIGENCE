# 32 Linear regression
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
X=np.array([[1],[2],[3],[4],[5]]);y=np.array([2,4,5,4,6])
m=LinearRegression().fit(X,y);p=m.predict(X)
print("slope",m.coef_[0],"intercept",m.intercept_,"MSE",mean_squared_error(y,p))
# 16 Feedforward neural network
from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X,y=make_moons(n_samples=300,noise=.2,random_state=1);a,b,c,d=train_test_split(X,y,random_state=1)
m=MLPClassifier(hidden_layer_sizes=(16,8),max_iter=1500,random_state=1).fit(a,c)
print(accuracy_score(d,m.predict(b)))
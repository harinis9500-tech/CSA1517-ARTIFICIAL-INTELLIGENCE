# 50 Genetic algorithm evolves a tiny neural network for XOR
import random,math
random.seed(4);data=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
sig=lambda x:1/(1+math.exp(-max(-30,min(30,x))))
def pred(g,a,b):
 h1=sig(g[0]*a+g[1]*b+g[2]);h2=sig(g[3]*a+g[4]*b+g[5])
 return sig(g[6]*h1+g[7]*h2+g[8])
def fit(g):return -sum((pred(g,a,b)-y)**2 for a,b,y in data)
pop=[[random.uniform(-2,2) for _ in range(9)] for _ in range(60)]
for _ in range(250):
 pop.sort(key=fit,reverse=True);new=pop[:6]
 while len(new)<60:
  p,q=random.sample(pop[:20],2);new.append([random.choice([p[i],q[i]])+random.gauss(0,.15) for i in range(9)])
 pop=new
g=max(pop,key=fit)
for a,b,y in data:print((a,b),"target",y,"prediction",round(pred(g,a,b),3))
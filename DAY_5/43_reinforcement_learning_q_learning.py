# 43 Q-learning in a one-dimensional world
import numpy as np,random
Q=np.zeros((6,2));alpha=.2;gamma=.9
for _ in range(500):
 s=0
 for t in range(20):
  a=random.randrange(2) if random.random()<.2 else int(np.argmax(Q[s]))
  ns=max(0,s-1) if a==0 else min(5,s+1);r=10 if ns==5 else -1
  Q[s,a]+=alpha*(r+gamma*max(Q[ns])-Q[s,a]);s=ns
  if s==5:break
print(Q.round(2));print("Best action at start:",np.argmax(Q[0]))
# 37 Genetic algorithm function optimization
import random
random.seed(3)
fit=lambda x:x*x*(10-x)
p=[random.uniform(0,10) for _ in range(30)]
for _ in range(60):
 p.sort(key=fit,reverse=True);parents=p[:10];n=parents[:2]
 while len(n)<30:n.append(max(0,min(10,(random.choice(parents)+random.choice(parents))/2+random.gauss(0,.3))))
 p=n
print("Best x and fitness:",max(p,key=fit),max(map(fit,p)))
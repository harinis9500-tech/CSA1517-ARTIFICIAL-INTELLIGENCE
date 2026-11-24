# 45 Markov chain weather simulation
import random
T={"Sunny":[("Sunny",.8),("Rainy",.2)],"Rainy":[("Sunny",.4),("Rainy",.6)]}
random.seed(10);s="Sunny";seq=[s]
for _ in range(20):
 names,weights=zip(*T[s]);s=random.choices(names,weights)[0];seq.append(s)
print(seq);print("Sunny:",seq.count("Sunny"),"Rainy:",seq.count("Rainy"))
# 09 Travelling Salesperson — brute force
from itertools import permutations
d=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
best=min(((sum(d[p[i]][p[i+1]] for i in range(4)),p) for p in [(0,)+x+(0,) for x in permutations([1,2,3])]))
print("Cost and tour:",best)
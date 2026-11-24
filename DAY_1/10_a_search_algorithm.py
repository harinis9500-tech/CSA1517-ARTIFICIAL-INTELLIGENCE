# 10 A* shortest path
import heapq
g={"A":{"B":1,"C":4},"B":{"C":2,"D":5},"C":{"D":1},"D":{}}
h={"A":4,"B":2,"C":1,"D":0}
q=[(h["A"],0,"A",["A"])]
while q:
 f,c,u,p=heapq.heappop(q)
 if u=="D":print(p,c);break
 for v,w in g[u].items():heapq.heappush(q,(c+w+h[v],c+w,v,p+[v]))
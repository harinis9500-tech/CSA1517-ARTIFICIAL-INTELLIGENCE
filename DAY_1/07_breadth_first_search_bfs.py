# 07 Breadth First Search
from collections import deque
g={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":[],"F":[]}
def bfs(s):
 q=deque([s]);seen={s}
 while q:
  u=q.popleft();print(u,end=" ")
  for v in g[u]:
   if v not in seen:seen.add(v);q.append(v)
bfs("A")
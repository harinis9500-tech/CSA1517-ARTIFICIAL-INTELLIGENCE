# 05 Missionaries and Cannibals — BFS
from collections import deque
moves=[(2,0),(0,2),(1,1),(1,0),(0,1)]
def valid(m,c):return 0<=m<=3 and 0<=c<=3 and (m==0 or m>=c) and (3-m==0 or 3-m>=3-c)
q=deque([((3,3,0),[(3,3,0)])]);seen={(3,3,0)}
while q:
 (m,c,b),p=q.popleft()
 if (m,c,b)==(0,0,1):print(p);break
 for x,y in moves:
  nm,nc=(m-x,c-y) if b==0 else (m+x,c+y);s=(nm,nc,1-b)
  if valid(nm,nc) and s not in seen:seen.add(s);q.append((s,p+[s]))
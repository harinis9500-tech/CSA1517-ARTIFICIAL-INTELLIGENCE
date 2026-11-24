# 03 Water Jug — BFS
from collections import deque
def solve(A=4,B=3,target=2):
 q=deque([((0,0),[(0,0)])]);seen={(0,0)}
 while q:
  (a,b),p=q.popleft()
  if a==target or b==target:return p
  x=min(a,B-b);y=min(b,A-a)
  for s in [(A,b),(a,B),(0,b),(a,0),(a-x,b+x),(a+y,b-y)]:
   if s not in seen:seen.add(s);q.append((s,p+[s]))
print(solve())
# 01 Eight Puzzle — A* search
import heapq
start=(1,2,3,4,0,6,7,5,8); goal=(1,2,3,4,5,6,7,8,0)
def h(s): return sum(abs(i//3-(v-1)//3)+abs(i%3-(v-1)%3) for i,v in enumerate(s) if v)
q=[(h(start),0,start,[])]; seen={start:0}
while q:
 f,g,s,path=heapq.heappop(q)
 if s==goal: print("Moves:",path); break
 z=s.index(0); r,c=divmod(z,3)
 for dr,dc,m in [(-1,0,"Up"),(1,0,"Down"),(0,-1,"Left"),(0,1,"Right")]:
  nr,nc=r+dr,c+dc
  if 0<=nr<3 and 0<=nc<3:
   j=nr*3+nc;t=list(s);t[z],t[j]=t[j],t[z];t=tuple(t)
   if g+1<seen.get(t,999):
    seen[t]=g+1;heapq.heappush(q,(g+1+h(t),g+1,t,path+[m]))
# 14 Alpha-beta pruning
def ab(vals,depth,alpha,beta,maximizing):
 if depth==0:return vals[0]
 mid=len(vals)//2
 if maximizing:
  v=float("-inf")
  for part in (vals[:mid],vals[mid:]):
   v=max(v,ab(part,depth-1,alpha,beta,False));alpha=max(alpha,v)
   if beta<=alpha:break
  return v
 v=float("inf")
 for part in (vals[:mid],vals[mid:]):
  v=min(v,ab(part,depth-1,alpha,beta,True));beta=min(beta,v)
  if beta<=alpha:break
 return v
print(ab([3,5,6,9,1,2,0,-1],3,float("-inf"),float("inf"),True))
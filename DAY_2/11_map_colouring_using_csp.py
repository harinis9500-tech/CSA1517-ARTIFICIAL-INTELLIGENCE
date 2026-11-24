# 11 Map colouring CSP
regions=["A","B","C","D"];adj={"A":["B","C"],"B":["A","C","D"],"C":["A","B","D"],"D":["B","C"]}
colors=["Red","Green","Blue"];ans={}
def colour():
 if len(ans)==4:return True
 r=next(x for x in regions if x not in ans)
 for c in colors:
  if all(ans.get(n)!=c for n in adj[r]):
   ans[r]=c
   if colour():return True
   del ans[r]
 return False
print(ans if colour() else "No solution")
# 08 Depth First Search
g={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":[],"F":[]}
def dfs(u,seen=None):
 if seen is None:seen=set()
 if u in seen:return
 seen.add(u);print(u,end=" ")
 for v in g[u]:dfs(v,seen)
dfs("A")
# 13 Minimax on a small game tree
def minimax(vals,depth,maximizing):
 if depth==0:return vals[0]
 mid=len(vals)//2
 a=minimax(vals[:mid],depth-1,not maximizing);b=minimax(vals[mid:],depth-1,not maximizing)
 return max(a,b) if maximizing else min(a,b)
print("Best value:",minimax([3,5,6,9,1,2,0,-1],3,True))
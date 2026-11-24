# 02 Eight Queens — backtracking
N=8; board=[-1]*N
def solve(r=0):
 if r==N:return True
 for c in range(N):
  if all(board[i]!=c and abs(board[i]-c)!=r-i for i in range(r)):
   board[r]=c
   if solve(r+1):return True
   board[r]=-1
 return False
solve()
for r in range(N):print(" ".join("Q" if board[r]==c else "." for c in range(N)))
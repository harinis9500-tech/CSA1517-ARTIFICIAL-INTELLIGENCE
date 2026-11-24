# 40 User-based collaborative filtering
import numpy as np
R=np.array([[5,4,0,1],[4,0,0,1],[0,5,4,0],[1,1,5,4]],float)
S=np.nan_to_num(np.corrcoef(R));u=0
scores=S[u]@R/(abs(S[u]).sum() or 1)
print("Recommended item indexes:",sorted(np.where(R[u]==0)[0]+1,key=lambda i:scores[i-1],reverse=True))
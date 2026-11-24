# 04 Cryptarithmetic SEND + MORE = MONEY
from itertools import permutations
for p in permutations(range(10),8):
 d=dict(zip("SENDMORY",p))
 if d["S"] and d["M"]:
  a=1000*d["S"]+100*d["E"]+10*d["N"]+d["D"]
  b=1000*d["M"]+100*d["O"]+10*d["R"]+d["E"]
  c=10000*d["M"]+1000*d["O"]+100*d["N"]+10*d["E"]+d["Y"]
  if a+b==c:print(a,b,c);break
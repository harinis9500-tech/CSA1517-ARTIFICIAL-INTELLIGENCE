# 12 Tic Tac Toe
b=[" "]*9;wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
for turn in range(9):
 print("\n".join("|".join(b[i:i+3]) for i in (0,3,6)))
 try:p=int(input("Position 1-9: "))-1
 except ValueError:continue
 if p not in range(9) or b[p]!=" ":print("Invalid");continue
 b[p]="X" if turn%2==0 else "O"
 if any(b[a]==b[c]==b[d]!=" " for a,c,d in wins):print(b[p],"wins");break
else:print("Draw")
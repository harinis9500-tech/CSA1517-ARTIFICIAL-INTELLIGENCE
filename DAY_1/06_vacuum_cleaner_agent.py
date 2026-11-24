# 06 Vacuum cleaner agent
rooms={"A":"Dirty","B":"Dirty"}; location="A"
while "Dirty" in rooms.values():
 if rooms[location]=="Dirty":print("Suck",location);rooms[location]="Clean"
 else:location="B" if location=="A" else "A";print("Move",location)
print(rooms)
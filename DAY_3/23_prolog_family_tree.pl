% 23 Family tree
father(ravi,arun). mother(meena,arun). father(ravi,priya). mother(meena,priya).
father(arun,kiran). mother(divya,kiran).
parent(X,Y):-father(X,Y). parent(X,Y):-mother(X,Y).
sibling(X,Y):-parent(P,X),parent(P,Y),X\=Y.
grandparent(X,Z):-parent(X,Y),parent(Y,Z).
% Query: ?- grandparent(ravi,kiran).
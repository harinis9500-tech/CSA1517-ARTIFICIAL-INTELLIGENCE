% 27 Best-first search (greedy)
edge(a,b). edge(a,c). edge(b,d). edge(b,e). edge(c,f). edge(e,g). edge(f,g).
heuristic(a,6). heuristic(b,4). heuristic(c,3). heuristic(d,5). heuristic(e,2). heuristic(f,1). heuristic(g,0).
best_first(S,G,P):-path([S],G,R),reverse(R,P).
path([G|T],G,[G|T]).
path([X|T],G,P):-findall(H-[Y,X|T],(edge(X,Y),\+member(Y,[X|T]),heuristic(Y,H)),L),keysort(L,[_-N|_]),path(N,G,P).
% Query: ?- best_first(a,g,P).
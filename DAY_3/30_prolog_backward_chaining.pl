% 30 Backward chaining: recursive ancestor proof
parent(john,mary). parent(mary,sam). parent(sam,tina).
ancestor(X,Y):-parent(X,Y).
ancestor(X,Y):-parent(X,Z),ancestor(Z,Y).
% Query: ?- ancestor(john,tina).
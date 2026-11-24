% 17 Prolog sum from 1 to N
sum_n(0,0).
sum_n(N,S) :- N>0, N1 is N-1, sum_n(N1,T), S is T+N.
% Query: ?- sum_n(5,S).
% 21 Towers of Hanoi
hanoi(1,A,B,_) :- write(A),write(' -> '),writeln(B).
hanoi(N,A,B,C) :- N>1,M is N-1,hanoi(M,A,C,B),hanoi(1,A,B,C),hanoi(M,C,B,A).
% Query: ?- hanoi(3,left,right,middle).
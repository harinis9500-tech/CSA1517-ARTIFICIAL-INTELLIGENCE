% 25 Monkey and banana planning
move(state(middle,on_box,middle,no),grasp,state(middle,on_box,middle,yes)).
move(state(P,on_floor,P,no),climb,state(P,on_box,P,no)).
move(state(P,on_floor,B,no),push_box(P,B),state(B,on_floor,B,no)).
move(state(P,on_floor,B,no),walk(P,Q),state(Q,on_floor,B,no)) :- P\=Q.
plan(S,[]) :- S=state(_,_,_,yes).
plan(S,[A|T]) :- move(S,A,N),plan(N,T).
% Query: ?- plan(state(middle,on_box,middle,no),P).
% 22 Bird can fly
bird(sparrow). bird(pigeon). bird(ostrich). bird(penguin).
cannot_fly(ostrich). cannot_fly(penguin).
can_fly(B) :- bird(B), \+ cannot_fly(B).
% Query: ?- can_fly(sparrow).
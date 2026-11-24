% 29 Forward chaining illustration
fact(a). fact(b).
rule(c):-fact(a),fact(b).
rule(d):-rule(c),fact(a).
derived(X):-fact(X). derived(X):-rule(X).
% Query: ?- derived(X).
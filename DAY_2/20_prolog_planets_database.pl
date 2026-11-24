% 20 Planets database
planet(mercury,terrestrial). planet(venus,terrestrial). planet(earth,terrestrial).
planet(mars,terrestrial). planet(jupiter,gas_giant). planet(saturn,gas_giant).
planet(uranus,ice_giant). planet(neptune,ice_giant).
outer_planet(P) :- planet(P,gas_giant).
outer_planet(P) :- planet(P,ice_giant).
% Query: ?- outer_planet(P).
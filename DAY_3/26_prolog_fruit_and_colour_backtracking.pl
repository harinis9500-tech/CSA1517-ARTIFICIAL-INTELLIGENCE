% 26 Fruit and colour backtracking
fruit(apple). fruit(banana). fruit(grape).
color(apple,red). color(banana,yellow). color(grape,purple).
fruit_color(F,C):-fruit(F),color(F,C).
% Query: ?- fruit_color(F,C).
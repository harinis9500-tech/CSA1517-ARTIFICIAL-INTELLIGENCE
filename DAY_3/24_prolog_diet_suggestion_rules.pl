% 24 Diet suggestion rules (educational only)
advice(diabetes,'high-fibre foods and controlled carbohydrates').
advice(anaemia,'iron-containing foods such as beans and leafy greens').
advice(hypertension,'lower-sodium foods such as fresh vegetables').
diet(Condition,Advice):-advice(Condition,Advice).
% Query: ?- diet(diabetes,A). Not medical advice.
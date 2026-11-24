% 28 Medical diagnosis rules (educational only)
symptom(p1,fever). symptom(p1,cough). symptom(p1,body_pain).
symptom(p2,sneezing). symptom(p2,runny_nose).
possible_condition(P,flu_like):-symptom(P,fever),symptom(P,cough),symptom(P,body_pain).
possible_condition(P,cold):-symptom(P,sneezing),symptom(P,runny_nose).
% Query: ?- possible_condition(p1,D). Not a real diagnosis.
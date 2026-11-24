% 19 Student teacher subject database
student(101,arun). student(102,meena).
teacher(t01,rao). subject(cs101,artificial_intelligence).
teaches(t01,cs101). enrolled(101,cs101). enrolled(102,cs101).
student_subject(N,S) :- student(I,N),enrolled(I,C),subject(C,S).
% Query: ?- student_subject(Name,Subject).
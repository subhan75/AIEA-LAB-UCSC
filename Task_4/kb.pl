% Defining male members
male(john).
male(michael).
male(robert).
male(david).

% Defining female members
female(susan).
female(emily).
female(anna).
female(linda).

% Defining parent-child relationships
parent(john, michael).
parent(john, emily).
parent(susan, michael).
parent(susan, emily).
parent(robert, john).
parent(linda, john).
parent(david, susan).
parent(anna, susan).

% Defining relationships
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
son(X, Y) :- parent(Y, X), male(X).
daughter(X, Y) :- parent(Y, X), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

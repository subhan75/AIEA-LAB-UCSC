% Facts: Some animals and their characteristics
mammal(dog).
mammal(cat).
mammal(elephant).
mammal(whale).

bird(eagle).
bird(parrot).
bird(penguin).

amphibian(frog).
amphibian(salamander).

can_fly(eagle).
can_fly(parrot).

has_fur(dog).
has_fur(cat).

lives_in_water(whale).
lives_in_water(penguin).
lives_in_water(frog).
lives_in_water(salamander).

% Rule: An animal is an amphibian if it is classified as one
amphibian(X) :- lives_in_water(X), \+ mammal(X), \+ bird(X).
 
#Animal classification prolog code with knowledge base and rules.
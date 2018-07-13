animals = ["Tiger","Lion","Bear","Cat","Dog","Rat"]
my_animals  = ["Cat","Dog"]
not_my_animals = []
for animal in animals:
    if animal not in my_animals:
        not_my_animals.append(animal)

print not_my_animals
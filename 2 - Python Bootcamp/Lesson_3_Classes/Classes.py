# Object Oriented Programming
# Working with classes, the way to create our own objects

import numpy as np


class Sample:
    pass


my_sample = Sample()

print('my_sample type is: ', type(my_sample))
print('\n')


class Cat:

    def __init__(self, breed):
        self.breed = breed


my_cat = Cat(breed='Siamese')

print('my_cat type is: ', type(my_cat))
print('my_cat attribute is: ', my_cat.breed)
print('\n')


class Dog:

    def __init__(self, breed, name, spots):  # Breed it's a parameter, it's also an argument

        # __init__ It's a constructor, it's going to be called automatically right after the object has been created
        # The keyword "self" it represents the instance of the object itself

        self.breed = breed
        self.name = name
        self.spots = spots

        # Attribute are characteristics from the objects, in this case it's self.breed
        # We take in the argument, in this case it's breed
        # We assign it using self.attribute_name

        # The arguments can be different objects, string objects, integer, float, boolean...

        # If we define 3 arguments in the constructor, we'll have to pass three parameters


my_neighbour_dog = Dog(breed='Lab', name='Lucas', spots=False)
my_dog = Dog('Mix', 'Miro', False)

print("my_neighbour_dog's class is: ", type(my_neighbour_dog))
print("my_dog's class is: ", type(my_dog))
print('\n')

print('my_dog breed is: ', my_dog.breed)
print('my_dog name is: ', my_dog.name)
print('my_dog has spots: ', my_dog.spots)
print('\n')


class Bird:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF THE CLASS
    # We don't have to use the self keyword, because it's a reference to a particular instance.
    species = 'Aves'

    # We can define an attribute as a class object level, foe example, a bird, no matter what name, breed or colors,
    # it's going to be always an Aves, or a dog a Mammal...
    # So instead, of defining a particular instance where we have to define that our dog it's a mammal,
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots


my_bird = Bird(breed='parrot', name='perki', spots=False)
my_bird.name

print("my_bird's type is: ", type(my_bird))
print('')
print("my_bird's breed is: ", my_bird.breed)
print("my_bird's name is: ", my_bird.name)
print("my_bird has spots: ", my_bird.spots)
print("my_bird's species is: ", my_bird.species, ", and all my bird instances are going to be ", my_bird.species)
print("\n")

my_neighbour_bird = Bird(breed='cacatua', name='pco', spots=True)

print("my_neighbour_bird's spice is: ", my_neighbour_bird.species)


# METHODS
# Methods are functions defined inside the body of a class. They are used to perform operations with the
# attributes of our objects. Methods are a key concept of the OOP paradigm. They are essential to dividing
# responsibilities in programming, especially in large applications.


class Doggy:
    specie = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # OPERATIONS/Actions --> Methods
    # Methods are functions defined inside of a class
    def bark(self, age):  # We can ask for some parameter when we call our method, like age
        print('Woof! My name is {} and I am {} years old'.format(self.name, age))  # self key is no longer needed
        # here, because we are passing the age as a parameter in the method, 'cause is not referencing any attribute
        # for that instance of the class


my_doggy = Doggy('Lab', 'Lucas')

my_doggy.bark(5)
print('\n')


class Circle:
    # Class object attribute
    pi = np.pi

    def __init__(self, radius=1):  # We pass the to the radius parameter the default value of 1

        self.radius = radius
        self.area = self.radius * self.radius * Circle.pi  # We can reference the class object attributes as,
        # name_class.name_attribute

    # Methods
    def get_circumference(self):
        return 2 * self.pi * self.radius


my_circle = Circle(8)

print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())
print('\n')

# INHERITANCE & POLYMORPHISM

class Animal:  # We'll call to the class that we want to use in an other class, base class

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()
print('\n')


class Doggo(Animal):  # We inherit the base class in the Dog class, it's known as a derived class

    def __init__(self):
        Animal.__init__(self)  # So I'm going to create an instance of the animal class when I create an instance
        # on my Doggo class. I'm able to do that because i'm inheriting from the animal class
        print('Doggo Created')

    # We can rewrite the functions,
    def who_am_i(self):
        print('I am a Dog')

    def bark(self):
        print('WOOF!')


my_doggo = Doggo()
my_doggo.who_am_i()
my_doggo.eat()
print('\n')


# POLYMORPHISM

# polymorphism refers to the way in which different object classes can share the same method name, and those methods
# can be called from the same place even though a variety of different objects might be passed in.

class Dinosaur:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says warg'


class Fish:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says gluglu'


alan = Dinosaur('Alan')
nemo = Fish('Nemo')

print(alan.speak())
print(nemo.speak())
print('\n')

# PROBE THE POLYMORPHISM

for pet in [alan, nemo]:
    print(type(pet))
    print(pet.speak())
    print(type(pet.speak()))

print('\n')
def pet_class(pet):
    print(pet.speak())

pet_class(alan)
pet_class(nemo)
print('\n')
# So in both cases we're able to pass in different objects (Dinasour and Fish) and we obtain object specific results
# from the same mechanism that same method call.

# We can use abstract classes and inheritance, which are those ones that we never expect to instantiate, it only serve
# as a base class


class Insect:
    # This class it will never expect to be instantiate it , my_insect = Insect()
    def __init__(self, name):
        self.name = name

    def speak(self):
        return NotImplemented("Subclass must implement this abstract method ")

# This will give us an error
# my_insect = Insect('bichi')
# my_insect.speak()


class Bee(Insect):

    def speak(self):
        return self.name + ' says bsss'


class Fly(Insect):

    def speak(self):
        return self.name + ' says bsss'


iris = Bee('Iris')
paul = Fly('Paul')

print(iris.speak())
print(paul.speak())

# SPECIAL METHODS
# How to use built in methods such as len, or print

my_lst = [1, 2, 3]

print(my_lst)
print(len(my_lst))


class Sample:
    pass


my_sample = Sample()

print(my_sample)  # It's going to print where is located the Sample object in memory
# print(len(my_sample))  Erro: object of type 'Sample' has no len(). We don't have this method in our class
print('\n')


class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages


b = Book('Python bases', 'Alex', 350)
print('Book class, whithout string representation')
print(b)  # What is the string representation of b?
# If I ask for the string representation of b, str(b). It will output he same result as print() but as a str,
# between quotation marks
print(str(b))
print('\n')



class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): # We can define a string representation for our class with __str__, so whenever we ask for the
        # string representation for our class, it will print whatever we define in that method.
        return f"{self.title} by {self.author} "

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')



my_book = Book('Python advanced', 'Alex Abades', 450)
print('Book class with string representation: ')
print(my_book)  # All it does the print method is print the what the sring representation "str()" returns back
print(len(my_book))

# DELETE

# If we want to delete an object of a determinate class of our memory we use "del", in this case we want to delete
# the my_book object from the Book class

del my_book

print(my_book)
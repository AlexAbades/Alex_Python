# Review


class Rectangle:  # We create our object

    # We want our initializer. The initializer method runs once the object has been created. The first argument of the
    # # method it has to be the object itself. Self means the instance the instance that has just been created.
    # (width, height) We are going to set attributes of the class. In this case they are going to be
    # value attributes so we call them properties as a pose to methods which are callable essentially

    def __init__(self, width, height):
        self.width = width
        self.heigth = height


# We create an instance of that class
print("First instance, only properties")
r1 = Rectangle(10, 20)
print(r1.width)

r1.width = 100

print(r1.width)

# we are going to define a class with 2 properties and 2 methods
print("\n\n2nd instance with two added methods")


class Rectangle:  # We create our object
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    # Adding attribute that are actually callable or method. We are going to define our first methods. They are
    # basically just functions but  they are special functions because they are called using this dot (.) notation
    def area(self):
        return self.width * self.heigth

    def perimeter(self):
        return 2 * (self.width + self.heigth)


r1 = Rectangle(10, 20)

print(r1.area())  # It's a callable, we have to make sure they are called

print(r1.perimeter())

# What's the string representation of our class??
print("\n\nString representation of our instance of rectangle's class")

print(r1)
# We can get the memory address with:
print(hex(id(r1)))


class Rectangle:  # We create our object
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # We can rewrite the str method, so when we print an instance of our class we can specify what we want to show
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    # We can also change the string representation, to get how the instance was created (exclusive of jupyter)
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)


r1 = Rectangle(10, 20)
print('\n\nString method changed')
print(r1)

# The string representation typically it's a string that shows how you will build the object again. How we actually
# instantiate this object. Exclusive for Jupyter notebook
print('\n\nString representation changed')
print(str(r1))

# Equality
r2 = Rectangle(10, 20)
print('\n')
print('Is r1 not equal to r2: ', r1 is not r2)
# They are different objects, they have different memory addresses, different instances of the class, different objects

# But why they are not equal if they have the same values?
print('\nHave they the same value?')
print(r1 == r2)


# We have the special method __eq__


class Rectangle:  # We create our object
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    # As it is comparing two objects, this method need the object itself(self) and the object which it's comparing
    # to (other).
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
        # We could also do it with tuple unpacking
        # return (self.width, self.height) == (other.width, other.height)


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

print('\nAre they the same object? ', r1 is r2)
print('\n\n', r1 is not r2)

print('\n\nHave they the same value? ', r1 == r2)

# With that we have problem, if we try to compare one Rectangle's instance, like r1, with another thing that is not
# an instance, we will get an error. It would say us that the object that we've passed doesn't have the width property.
# It really will say attribute, but remember that a value attribute is a property
print('\n\nError r1 == 100:')
# print(r1 == 100)
print("AttributeError: 'int' object has no attribute 'width'")


class Rectangle:  # We create our object
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        # We'd like to check if they are instance instead of checking the type, to not be too much restrictive
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

print('\n\n', r1 == r2)

print('\n\n', r1 == r2)


# We have also methods for the other operators, like: lt(less than) <; le(less than or equal) <=, gt(greater than)...


class Rectangle:  # We create our object
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other._width and self.height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 20)

print('\nIs r1 less than r2:', r1 < r2)
print('\nIs r2 less than r1? ', r2 < r1)

# what if we implement the greater operator?
print('\nIs r2 grater than r1? ', r2 > r1)


# It works because what python does is: if the greater operator is not implemented, python will flip the values around
# and compare instead: r1 < r2.


class Rectangle:  # We create our object
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other._width and self.height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


# What if somebody changes the width property to a negative value?

r1 = Rectangle(10, 20)
print('\n', r1)

# We are allowing direct acces to the properties
r1.width = -100

print('\n', r1)


# It really have no sense set width negative or zero values.

# What we could do is make the properties private. And we can't really do that, because in python we can't create
# private properties, but we can do is name them with de convention of private properties, so the other users can see
# that they are private and they don't have to mess with them unless they really know what they are doing.
# We can encourage people to use instead the getters and setters


################################################################
# The get_width; set_width are JAVA conventions. You must specify them at the moment you create the class
################################################################
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be possitive')
        else:
            self._width = width

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)

# print('\n\n', r1.width) This will give an error: AttributeError: 'Rectangle' object has no attribute 'width'

print('\nRectangle width: ', r1._width)

r1.set_width(100)
print(r1)


#############################################################
# END of Java conventions
#############################################################

# Python allows to change, or stop people putting wrong values without breaking the compatibility. So you don't have
# to start with getters and setters. And istead of a getter and setter we'd use properties (we'll talk about them later)


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    # even if both function have the same name, they aren't the same (They aren't stepping on each other toes) because
    # the decorator.
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


#########
# Another thing to notice is, even we have the properties as pseudo private classes: _width; _height all the methods and
# like __lt__, __str__, area... are implemented with the get method; .width & .height. That is because if we call the
# width method, we are actually calling the property def width, which it really returns the self._width. So it's
# setting the width using the getters and setters, and we are filtering the values with their logic.

r1 = Rectangle(10, 20)

print('\n', r1.width)

print('\n', r1.width)  # It's actually getting the width form the width method.
# Notice the difference, even if it's method, we didn't call it. The methods are called with parentheses. That is
# because we've used the property, python now is able to access the width via the getter and we haven't had to change
# any code that was actually using .width as the direct access to the property before.
# So now we have a method that goes through a method (a getter) without breaking backward compatibility


# We can't set negative values: r1.width = -100
r1.width = 100
print('\n', r1)


# ###################
# With the code above we can instantiate an object of the rectangle class with negative values, what we could do
# instead, is call the setters inside my init method

class Rectangle:
    def __init__(self, width, height):
        self.width = width  # we are calling the width setter
        self.height = height  # We are calling the height setter

    @property
    def width(self):
        return self._width

    # Even if both function have the same name, they aren't the same (They aren't stepping on each other toes) because
    # the decorator.
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(-100, 20)

from collections import Counter

my_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

# If we want to count the number that a number appears. We couls create a for loop with a dictionary to crate that

print(Counter(my_list))

mylist = ' a a a a a a b b b b b b c c c c'.split()

print(Counter(mylist))

# Counter is technically a dictionary subclass that essentially helps to count cashable objects
# Where the key is the object and the value the count

print(Counter('aaaabbbbssssdfj'))

print(Counter('How many times appears a word in this sentence'.lower().split()))

letters = 'aaaaaaabbbbbbbbbcccccccdddddd'

c = Counter(letters)

print(c)

print(c.most_common())
print('')
print(c.most_common(2))

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts


print('')
print(list(c))


from collections import defaultdict
# What it's going to do is assign a default value for a kay that we had not specified


d = {'a': 10}
print(d['a'])
try:
    print(d['wrong'])
except KeyError:
    print("KeyError: 'wrong'")

d = defaultdict(lambda: 0)

# If we try to access a specific key that we haven't specified it will return the value
print('\n')
d['correct'] = 100
print(d)
print(d['correct'])
print(d['wrong'])
print('\n\n\n')

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name']) # We create a dog object

print(Dog)
print('')

sammy = Dog(age=5, breed='husky', name='sammy')
print(type(sammy))
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy.name)
print(sammy[0])
print(sammy[1])
print(sammy[2])

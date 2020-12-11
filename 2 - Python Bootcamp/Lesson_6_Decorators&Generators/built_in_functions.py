# Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the
# values in a list.


def word_lengths(phrase):
    return list(map(len, phrase.split()))


print(word_lengths('Hello my name is Alex'))


# Use reduce() to take a list of digits and return the number that they correspond to. For example, [1, 2,
# 3] corresponds to one-hundred-twenty-three. Do not convert the integers to strings!


from functools import reduce


def digits_to_number(lst):
    return reduce(lambda a,b: a*10 +b, lst)


print(digits_to_number([1,2,3,4]))
print(digits_to_number([5,4,2,1,6,3]))

# Use filter() to return the words from a list of words which start with a target letter.


def filter_word(word_list, letter):
    return list(filter(lambda word: word[0] == letter, word_list))


words = ['hello','are','cat','dog','ham','hi','go','to','heart']

print(filter_word(words, 'h'))


# Use zip() and a list comprehension to return a list of the same length where each value is the two strings from L1
# and L2 concatenated together with a connector between them. Look at the example output below:

def concatenate(lst1, lst2, connector):
    return [word+connector+word2 for word,word2 in zip(lst1,lst2) ]


print(concatenate(['A','B'],['a','b'],'-'))


# Use enumerate() and other skills to return a dictionary which has the values of the list as keys and the index as
# the value. You may assume that a value will only appear once in the given list.

def d_list(lst):
    return {key: value for value,key in enumerate(lst) }

print(d_list(['a','b','c']))


def count_match_index(lst):
    return len([num for count,num in enumerate(lst) if count==num])

print(count_match_index([0,2,2,1,5,5,6,7,10]))
#################
# GENERAL EXPRESSIONS
#################
# What we are going to de is specify the identifier: r"what_we_want_to_search"
# the inside the identifier, we have to specify the digit
# (555)-555-555
# r"(\d\d\d)-\d\d\d-\d\d\d\d"
# r"(\d{3})-\d{3}-\d{4}"
# The "r" before the string says that we aren't going to treat this as a normal sting

text = "The agent's phone number is 408-555-1234. Call soon!"

print("phone" in text)

import re

pattern = "phone"
print('Searching a pettern that it is in the text: ')
print(re.search(pattern=pattern, string=text))
print('')

print('Searching a pattern that is not in the text: ')
pattern = "Note in text"
print(re.search(pattern, text))
print('')

pattern = "phone"
match = re.search(pattern=pattern, string=text)
print(match)
print('')
print(match.span())
print(match.start())
print(match.end())
print('')

# The search function only returns the first match
# If we want to find all the matches we have to use:

text = 'My first phone, my second phone'
mateches = re.findall(pattern, text)
print(mateches)
# The problem it's that it only returns a list

# if we want to create Match object, we hace to create an interator

for match in re.finditer(pattern, text):
    print(match)
print('')
for match in re.finditer(pattern, text):
    print(match.span())
print('')
for match in re.finditer(pattern, text):
    print(match.group())
print('\n\n')
# CODES

# \d --> Digit
# \w --> Alphanumeric (it also includes the underscore)
# \s --> Whitespace
# \D --> Non Digit
# \W --> Non Alphanumeric
# \S --> Non Whitespace

text = "My phone number is 408-555-1234"
pattern = "408-555-1234"
phone = re.search(pattern, text)
print(phone)
print(phone.group())
print('')
# If we change the number in the text, it won't find it!


pattern = r"\d{3}-\d{3}-\d{4}"
phone = re.search(pattern, text)
text = "My phone number is 408-555-1777"
print(phone)
print(phone.group())
print('\n\n')

# QUANTIFIERS

# + --> Occurs more than once, we can use it at the end of a string
# {3} --> Occurs exactly a number of times, in this case 3.
# {2,4} --> Occurs between a range of number of times
# {3,} --> Occurs minimum 3 times but without a limit of times
# * --> Occurs zero or more times
# ? --> Once or none


# If we want to group some digits ot characters inside the pattern, for print them after,
# we have to use the compile function. For example we'll useit if we want to extract the number of phones
text_phone = ["+24-456-32-14-67",
              "+53-345-67-31-45",
              "+45-94-623-76-53",
              "+45-93-688-93-35",
              "+34-93-650-09-95"]

phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")  # The parentheses indicates that they're going to
# be a group of patterns, and it compiles it to the same group, but we can call the groups

results = re.search(phone_pattern, text)
print(results)
print(results.group())
print(results.group(1))
print(results.group(2))
print(results.group(3))
print('\n')

phone_num1 = text_phone[0]
print(phone_num1)
pattern = r"\+\d\d-"
phone1_prefix = re.match(pattern, "+34-93-650-09-95")
print(phone1_prefix)
print(phone1_prefix.group())
print('')

for num in text_phone:
    print(re.search(pattern, num).group())

print('\n\n')

# OR OPERATOR FOR SEARCHING PATTERNS
print('Or operators in regex')
cat = re.search('cat', 'I have a cat')
print(cat)
print(cat.group())

# What happens if we want to search if the owner has a cat or a dog?
# We need the pip operator

dog_cat = re.search('cat|dog', 'I have a dog')
print(dog_cat)
print(dog_cat.group())
print('\n')

# What happens if we find part of a string
print(re.findall(r'at', 'The cat in the hat sat there'))
# Truly there isn't the at preposition, how we can find a specific word?
print(re.findall(r' at', 'The cat in the hat sat there, try to attempt'))
print(re.findall(r' at ', 'The cat in the hat sat there, try to attempt'))
# We have to be very carefully!
# So, what we have to do if we want an specific letter in front of that pattern
print(re.findall(r'.at', 'The cat in the hat sat there'))
# The problem is that the wild card (the dot: . ) it's going to grab something always
print(re.findall(r'...at', 'The cat in the hat sat in the splat'))
print('\n\n')

# If the string starts with, for example a number, we can use the hat: ^ to find the string

print(re.findall(r'^\d', '1 is the first number, yes 1'))
# We can also search with what character ends
print(re.findall(r'\d$', 'The number is 2'))
print('')

# To exclude some characters, we can use the hat symbol with the square brackets
phrase = 'There are 3 numbers 34 inside 5 this phrase'
# Let's say that we want to exclude the numbers, so we want to return everything except the numbers
pattern = r'[^\d]'
purged_phrase = re.findall(pattern, phrase)
print(purged_phrase)
print(''.join(purged_phrase).replace('  ', ' '))
pattern = r'[^\d]+'
print(re.findall(pattern, phrase))
print('')

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(clean))
print('ºn')


#
text = 'Only find the hypen-word in this sentence. But do not know how long-ish they are'
# The main thing is that we don't know how many words are after and before the dash
pattern = r"[\w]+-[\w]+"
print(re.findall(pattern, text))
# The same result:
print(re.findall(r"\w+-\w+", text))

text = 'Hello, would you like some catfish'
texttwo = 'Hello would you like to take a catnap'
textthree = 'Hello, have you seen this caterpillar'

pattern = r"cat(fish|nap|erpillar)"

print(re.search(pattern, text))
print(re.search(pattern, texttwo))
print(re.search(pattern, textthree))




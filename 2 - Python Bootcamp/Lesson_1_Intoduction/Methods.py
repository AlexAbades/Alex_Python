lst = list(range(8))
print(lst)

lst.remove(6)
print(lst)
lst.insert(3,3)
print(lst)
lst.extend(lst)
print(lst)
lst.append(lst)
print(lst)
lst2 = list(range(10))
print(lst2)
print(lst2[-1])

def probe(num1, num2):
    return num1*num2+(num1*num2)

a = probe(4,5)
print(a)

print(12345-12245)

print(0.1+0.2-0.3)
print(1/2)
s='Hello World'
print(s[-3])

print(set('Mississippi'))

print(set([1, 1, 2 ,3]))


import requests
import bs4
import os


path = "D:\\Documentos\\Documentos User Admin\\4 - Cursos\\2 - Udemy\\2 - Python\\3 - Python 3 Deep Dive\\1 - Part " \
       "1\\3 - Numeric types\\2 - Exercises\\"
url = 'https://www.udemy.com/course/python-3-deep-dive-part-1/learn/lecture/7192366#questions/13325660/'
res = requests.get(url)
b = bs4.BeautifulSoup(res.text, 'lxml')

lst = ["Integers_Data Types",
       "Integers_Operations",
       "Integers_Constructors and Bases - Lecture",
       "Integers_Constructors and Bases - Coding",
       "Rational Numbers - Lecture",
       "Rationals Numbers - Coding",
       "Floats_Internal Representations - Lecture",
       "Floats_Internal Representations - Coding",
       "Floats_Equality Testing - Lecture",
       "Floats_Equality Testing - Coding",
       "Floats_Coercing to Integers - Lecture",
       "Floats_Coercing to Integers - Coding",
       "Floats_Rounding - Lecture",
       "Floats_Rounding - Coding",
       "Decimals - Lecture",
       "Decimals - Coding",
       "Decimals_Constructors and Contexts - Lecture",
       "Decimals_Constructors and Contexts - Coding",
       "Decimals_Math Operations - Lecture",
       "Decimals_Math Operations - Coding",
       "Decimals_Performance Considerations",
       "Complex Numbers - Lecture",
       "Complex Numbers - Coding",
       "Booleans",
       "Booleans_Truth Values - Lecture",
       "Booleans_Truth Values - Coding",
       "Booleans_Precedence and Short-Circuiting - Lecture",
       "Booleans_Precedence and Short-Circuiting - Coding",
       "Booleans_Boolean Operators - Lecture",
       "Booleans_Boolean Operators - Coding",
       "Comparison Operators"]


print(len(lst))


a = [str(x) for x in range(1,32)]
d = [None] * len(lst)

for i in range(len(lst)):
    d[i] = a[i] + ' - ' + lst[i]


print(d)


for i in range(len(lst)):
    os.makedirs(path + d[i])




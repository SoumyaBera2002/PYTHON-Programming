Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3
5
>>> 9 - 8
1
>>> 4*6
24
>>> 8/4
2.0
>>> 5/2
2.5
>>> 5//2
2
>>> 8+9-10
7
>>> ((8+9)/2)
8.5
>>> 2 ** 3
8
>>> 2 * 2 * 2
8
>>> 10 // 3
3
>>> 10 % 3
1
>>> 'Soumya'
'Soumya'
>>> print('Soumya's laptop')
      
SyntaxError: invalid syntax
>>> print("Soumya's laptop")
Soumya's laptop
>>> print('Soumya\'s "laptop"')
Soumya's "laptop"
>>> 'navin' + 'navin'
'navinnavin'
>>> 10 * ' navin'
' navin navin navin navin navin navin navin navin navin navin'
>>> print('c:\docs\navin')
c:\docs
avin
>>> print('c:\docs\\navin')
c:\docs\navin
>>> print(r'c:\docs\navin')
c:\docs\navin
>>> x = 2
>>> x + 3
5
>>> y = 3
>>> x + y
5
>>> x = 9
>>> x + y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x + 10
19
>>> 19 + y
22
>>> _ + y
25
>>> name = 'Soumya'
>>> name
'Soumya'
>>> name + 'Bera'
'SoumyaBera'
>>> name * 'B'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    name * 'B'
TypeError: can't multiply sequence by non-int of type 'str'
>>> name[0]
'S'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'a'
>>> name[-2]
'y'
>>> name[0:2]
'So'
>>> name[0:5]
'Soumy'
>>> name[2:6]
'umya'
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> 'my' + name[3:6]
'mymya'
>>> myname = 'SOUMYA BERA'
>>> len(myname)
11
>>> 
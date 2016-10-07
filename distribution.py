"""
distribution.py
Author: Bauti G
Credit: Vinzent

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
text=str.lower(input("Please enter a string of text (the bigger the better): "))
text2=text.replace(" ", "")
lis3=list(string.ascii_lowercase)

lis1 = []
lis1.append(text.count('a'))
lis1.append(text.count('b'))
lis1.append(text.count('c'))
lis1.append(text.count('d'))
lis1.append(text.count('e'))
lis1.append(text.count('f'))
lis1.append(text.count('g'))
lis1.append(text.count('h'))
lis1.append(text.count('i'))
lis1.append(text.count('j'))
lis1.append(text.count('k'))
lis1.append(text.count('l'))
lis1.append(text.count('m'))
lis1.append(text.count('n'))
lis1.append(text.count('o'))
lis1.append(text.count('p'))
lis1.append(text.count('q'))
lis1.append(text.count('r'))
lis1.append(text.count('s'))
lis1.append(text.count('t'))
lis1.append(text.count('u'))
lis1.append(text.count('v'))
lis1.append(text.count('w'))
lis1.append(text.count('x'))
lis1.append(text.count('y'))
lis1.append(text.count('z'))

lis2=list(range(0,26))

zipped=zip(lis1,lis2,lis3)
zipped=list(zipped)
zipped.sort(reverse=True)
number=0
number2=0

while number<26:
    if zipped[number][0] != 0:
        while number2<zipped[number][0]:
            for char in str(zipped[number][2]):
                print(char*(number2+1), end="")
            number2=number2+1
        number=number+1
        number2=0
        print()
    else:
        number=number+1


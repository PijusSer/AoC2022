from collections import Counter

buffer = open(r'C:\Users\Pijus\Desktop\ipython\1206\input.txt', 'r')
text = buffer.read()
buffer = open(r'C:\Users\Pijus\Desktop\ipython\1206\input.txt', 'r')

def isUniqueChars(string):
    freq = Counter(string)
    if(len(freq) == len(string)):
        return True
    else:
        return False

four = ()
fourteen = ()
i = 0
ii = 0

while i <= len(text):
    four = text[i:(i+4)]
    if isUniqueChars(four):
        print (i+4)
        i = len(text)
    i += 1
    
while ii <= len(text):
    fourteen = text[ii:(ii+14)]
    if isUniqueChars(fourteen):
        print (ii+14)
        ii = len(text)
    ii += 1
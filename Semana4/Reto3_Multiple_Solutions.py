# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:11:01 2021

@author: Andres Salazar
"""
### Count how many times I have a character in list
text = "V V C W W W W A A A A U U Z W W W W X A A A A T"

letters_chain = []
new_text = text.split()

for i in new_text:

    letter = new_text.index(i)
    letters_chain.append(letter)
    # print(letter)
    
res = [i for n, i in enumerate(letters_chain) if i not in letters_chain[:n]]

for j in res:
    
    l = new_text[j]
    c = text.count(l)
    print(c, end = " ")
    
#%% Count how many times I have one character in list

from collections import Counter

s = "V V C W W W W A A A A U U Z W W W W X A A A A T"
result = Counter(s)    


#%% Using group by

from itertools import groupby

text = "V V C W W W W A A A A U U Z W W W W X A A A A T"

new_text = text.split()

print(text)

print([len(list(j)) for i, j in groupby(new_text)])

# print(result)

#%% 

from itertools import groupby

text = "V V C W W W W A A A A U U Z W W W W X A A A A T"

new_text = text.split()

for i,j in groupby(new_text):
    
    print(i, end = " ")
    
print('\n')
# l = []
for i, j in groupby(new_text):
    
    # print(i)
    # l.append(i)
    print(len(list(j)), end = " ")
    
# str1 = ''.join(l)
# print(str1)

#%%

entrada = "V V C W W W W A A A A U U Z W W W W X A A A A T"
cadena1 = ""
cadena2 = ""
count = 0
tmp = ""

for x in entrada:
   if tmp == "":
     cadena1 += x + ' '
     count += 1
     tmp = x
   elif tmp==x:
      count+= 1
   elif x== ' ':
     continue
   else:
     cadena2 += str(count) + ' '
     count = 1
     cadena1 += x + ' '
     tmp = x


cadena2+=str(count)
print(cadena1.strip())
print(cadena2.strip())

#%%

text = "V V C W W W W A A A A U U Z W W W W X A A A A T"

new_text = text.split()

c_in = []
c_out = []
count = 0
l = []

for i in new_text:
    if l == []:
      c_in += i
      count += 1
      l = i
    elif l==i:
      count+= 1
    else:
      c_out.append(count)
      count = 1
      c_in += i
      l = i


c_out.append(count)

print(' '.join(map(str, c_in)))
print(' '.join(map(str, c_out)))

    
    
    
    
    
        
    


















    
    
    
    
    
    
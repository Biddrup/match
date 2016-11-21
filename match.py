#Will do some revision within a short time

import re

nameletter = re.compile(r'[biddrupBIDDRUP]')
b = nameletter.findall('My name is Biddrup Kumar Mallick')

escnameletter = re.compile(r'[^biddrupBIDDRUP^]')
c = escnameletter.findall('My name is Biddrup Kumar Mallick')

#'list' object has no attribute 'group'
#Can't convert 'list' object to str implicitly
#That's why I am taking 'str' to make that str
print('Here is the name letter: \n' + str(b))
print('Here is the escape name letter: \n' + str(c))

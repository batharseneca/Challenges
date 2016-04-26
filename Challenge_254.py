# SOLUTION IN PYTHONNN

import string


Input = 'gsrh rh zm vcznkov lu gsv zgyzhs xrksvi'


alphabet = list(string.ascii_lowercase)
atbash = list(reversed(string.ascii_lowercase))
ALPHABET = list(string.ascii_uppercase)
ATBASH = list(reversed(string.ascii_uppercase))
Output = []
for i in range(0,len(Input)):
    if Input[i] in alphabet:
        Output.append(atbash[alphabet.index(Input[i])])
    elif Input[i] in ALPHABET:
        Output.append(ATBASH[ALPHABET.index(Input[i])])
    else:
        Output.append(Input[i])

Outputstr = ''.join(Output)        
print Outputstr

'''
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: ZYXWVUTSRQPONMLKJIHGFEDCBA

INPUT:
foobar
wizard
/r/dailyprogrammer
gsrh rh zm vcznkov lu gsv zgyzhs xrksvi

OUTPUT:
ullyzi
draziw
/i/wzrobkiltiznnvi
this is an example of the atbash cipher

BONUS:
Preserve case.
'''
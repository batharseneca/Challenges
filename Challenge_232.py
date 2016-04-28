# input = '''4
# A man, a plan, 
# a canal, a hedgehog, 
# a podiatrist, 
# Panama!'''

# input = list(input.split("\n"))
# numsents = input[0]
# del input[0]
# input = "".join(input)
# input = input[:-1]
# input = input.replace(" ", "")
# input = input.lower()

# revinput = input[::-1]

# print input
# print revinput

# if (input == revinput):
    # print "PALINDROME"
# else:
    # print "NOT PALINDROME"


import re

numOfLines = input('How many lines you want, dude? ')

def checkPalindrome(inputtedText):
  # Make this shit lowercase
  inputtedText = inputtedText.lower()

  # Strip the string of everything but numbers, characters
  pattern = re.compile('[^a-z0-9]')
  inputtedText = re.sub(pattern, '', inputtedText)

  # Reverse the string and compare
  reversedText = ''.join(reversed(inputtedText))
  if inputtedText == reversedText:
    print "Palindrome"
  else:
    print "Not a palindrome"

inputtedText = ""
for x in range(0, numOfLines):
  inputtedText = inputtedText + raw_input()

checkPalindrome(inputtedText)
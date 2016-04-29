# input = '''STEAD'''

# alpha = "-abcdefghijklmnopqrstuvwxyz"
# input = input.split("\n")

# fortotal = 0
# backtotal = 0

# for word in input:
    # word = word.lower()
    # fortotal = alpha.index(word[0])
    # forind = 0
    # backtotal = alpha.index(word[-1])
    # backind = -1
    
    # print fortotal, backtotal, "\n"
    
    # for i in range (1,len(word)-1):
        # if fortotal > backtotal:
            # bal = forind + 1
            # backind = backind + 1
            
            # backtotal += alpha.index(word[((i+1)*-1)])
            # print fortotal, backtotal, "---------------------\n"
        # elif backtotal > fortotal:
            # bal = backind + 1
            # forind = forind + 1
            # fortotal += alpha.index(word[i])
            # print fortotal, backtotal, "++++++++++++++++++++++\n"
        # else:
            # if (len(word[:i]) == len(word[:-i])):
                # print "{} {} {} - {}".format(word[:i], word[i:i+1], word[-i:], fortotal)
            # else:
                # backtotal += alpha.index(word[((i+1)*-1)])
                # fortotal += alpha.index(word[i])
                # print "{} {} {} - {}".format(word[:i], word[i:i+1], word[-i:], fortotal)
            
# letters = 'abcdefghijklmnopqrstuvwxyz'


# def balance(word):
    # for mid in range(1, len(word) - 1):
        # left = sum((mid - i) * (letters.find(word[i].lower()) + 1) for i in range(mid))
        # right = sum((i - mid) * (letters.find(word[i].lower()) + 1) for i in range(mid + 1, len(word)))
        # if left == right:
            # print('{} {} {} - {}'.format(word[:mid], word[mid], word[mid + 1:], left))
            # return

    # print('{} does not balance'.format(word))


# balance('STEAD')
# balance('CONSUBSTANTIATION')
# balance('WRONGHEADED')
# balance('UNINTELLIGIBILITY')        
        
        
def string_weight(l):

    torque = 0

    # for every letter weight, multiply by index and add to total torque.
    for index, weight in enumerate(l):

        torque += (1+index) * weight

    return torque

def get_weight(char):

    alpha = 'abcdefghijklmnopqrstuvwxyz'

    return alpha.index(char) + 1

# Grab the input and make it all lower case
word = raw_input('Word: ').lower()

# Make a new array by replacing the letters with their weight a=1 b=2 etc
weights = [get_weight(char) for char in word]

for i in range(len(word)):

    # Calc the weight of both sides of the fulcrum, using i as the fulcrum
    # [:i] and [1+i:] are the snipped sides of the word
    # list(reversed(weights)) reverses the list (which I only found out was important after testing)
    left_sum = string_weight(list(reversed(weights[:i])))
    right_sum = string_weight(weights[1+i:])

    # The sides are balanced
    if left_sum == right_sum:

        print word[:i], word[i], word[1+i:], '-', left_sum
# string = "12 34 55"
# string = "".join(string.split())
# string = string.split()
# result = sorted(string)

# sorted()

# print "normal sorted: " + str(result)


# result = sorted(string, reverse=True) 

# print "reverse sorted: " + str(result)


word = raw_input()
print word, "IN ORDER" if word == "".join(sorted(word)) else "REVERSE ORDER"  if "".join(sorted(word)) == word[::-1] else "NOT IN ORDER"
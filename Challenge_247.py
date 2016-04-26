# SOLUTION IN PYTHONNN

import random

input1 ='''Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea'''

list2=list(input1.split("\n"))
count=1
list3 = {}
list4 = []
santa = {}
available = []

# for families in list2:
    # list3[count] = families
    # count = count + 1

# print list3

for items in list2:
    list5 = (list(items.split(" ")))
    for itemz in list5:
        list4.append(itemz)
        list3[itemz] = count
    count = count + 1
# print list4 #all names in a list
# print list3 #dictionary same families have same value
participants = len(list4) #number of participants
for i in range(participants):
    available.append(i)   
for i in range(participants):
    successful = False
    while not successful:
        pairing = random.choice(available)
        personpair = list4[pairing]
        person = list4[i]
        # print person + "-" + list4[i]     
        if (list3.get(personpair) != list3.get(person) and person != personpair):
            santa[person] = personpair
            # print santa 
            available.remove(pairing)            
            # print available
            successful = True
print "\n"      
for key in santa.keys():
    multi = len(key)
    multi = 15-multi
    multi = " "*multi
    space = " "*5
    print key + multi + "==>" + space + santa[key] 
            
            
            



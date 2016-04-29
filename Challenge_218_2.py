input='''123 286 196196871'''
input = input.split()
for number in input:
    count = 0
    total = number
    if int(number) == int(number[::-1]):
        print str(number) + " gets palindromic after " + str(count) + " steps: " + str(number)
        continue
    else:
        while not int(number) == int(str(number)[::-1]):            
            number = int(number) + int(str(number)[::-1])
            count += 1
        print str(total) + " gets palindromic after " + str(count) + " steps: " + str(number)    
        
        
        
        
        
        
'''       
challenge = [123, 286, 196196871]  

def make_pal(num):  
    return num + int(str(num)[::-1])  

def is_pal(num):  
    return num == int(str(num)[::-1])  

for i in challenge:  
    new_num = i  
    step = 0  
    while not is_pal(new_num):  
        new_num = make_pal(new_num)  
        step += 1  
    print(i, 'gets palindromic after', step, 'steps', new_num)  
'''
import os
os.system('clear')

count = 0
for count in range(100):  #using while(count < 100)
    count+= 1
    if(count % 3 == 0) and (count % 5 == 0):
        print("%s - FizzBuzz!!!" % count) 
    elif (count % 3 == 0):
        print("%s - Fizz!!" % count)
    elif(count % 5 == 0):
        print("%s - Buzz!!" % count)
    else:
        print(count)


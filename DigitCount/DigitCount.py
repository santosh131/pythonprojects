num =input("please enter the number")
result = len(str(num))

remainder =1
currentNumber =int(num)
result = 0
while(currentNumber!=0):    
    remainder = currentNumber % 10
    currentNumber =  (currentNumber - remainder) / 10
    result = result + 1
    
print("Number of digits in " + str(num) + " is " + str(result))
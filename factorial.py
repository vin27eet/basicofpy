#factorial of any number
fact=1
num = int(input("Enter a Number: ")) 
for  i in range(1, num + 1):   
    fact = fact * i  
    print(fact)
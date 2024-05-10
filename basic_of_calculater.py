n=input("enter the symbols")
print("the given symbols ")

if (n=='+') or (n=="add"):
    a=int(input("Enter first number:"))
    b=int(input("Enter second        number:"))
    print("The sum is",a+   b)
elif (n=='-' )or   (n=="subtract"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a-  b)
elif (n=='x' )or   (n=="multi"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a* b)
elif (n=='/' )or   (n=="division"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a/  b)
elif (n=='%' )or   (n=="modular"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a% b)
elif (n=='//' )or   (n=="floor division"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a//  b)
elif (n=='&' )or   (n=="and"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a& b)
elif (n=='|' )or   (n=="or"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a| b)
elif (n=='^' )or   (n=="power"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a** b)
elif (n=='xor' )or   (n=="exclusive or"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",a^  b)
elif (n=='root' )or   (n=="root"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("enter the root"))
     print("The sum is",a** (1/b))
elif (n=='~' )or   (n=="not"):   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     print("The sum is",~a)
elif (n=='herons' ) :   #checking for subtraction 
     a=int(input("Enter first number:"))
     b=int(input("Enter second        number:"))
     c=int(input("Enter second        number:"))
     s=(a+b+c)/100
     print("The sum is",(s*(s-a)*(s-b)*(s-c))**(1/2))
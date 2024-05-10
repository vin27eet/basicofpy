# n=int(input("enter the number--->"))
# x=int(input("enter the number--->"))
# y=0
# for i in range(n+1):
#       y+=x+i
#       print(y)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print (factorial(5))
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print (factorial(5))
#Question 1+x**1/1!+x**2/2!+----x**n/n!
n=int(input("Enter a value of n-->"))
x=int(input("Enter a value of x-->"))
fact=1
for i in range(1,n+1):
      fact=fact*i
      z=fact
y=1
for i in range(n+1):
    y+=x*n/z
    print(y)
    #2+x*2/2+x*4/4+x*6/6------x*2n/2n
      
    
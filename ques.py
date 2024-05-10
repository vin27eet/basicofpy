#if form
a=1
b=0
if(a==0 and b==0):
    print("0")
elif(a==0 and b==1):
    print("0")
elif(a==1 and b==0):
    print("0")
elif(a==1 and b==1):
    print("1")
else:
    print("not applicable in boolean F**n")
    
    #boolean form
    
a=bool(0)
b=bool(1)
print(a|b)
print(bool(a)&bool(b))
print(bool(a)|bool(b))

#all of and or
a=bool(0)
b=bool(1)
c=bool(0)
d=bool(1)
e=bool(0)
print((a&(b&c)|d)|e)



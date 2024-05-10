n=int(input("enter the principle amount"))


if (n<=10000) and (n>=5000):
    time=float(input("time--->"))
    rate=float(input("rate---> range between 1% to 5%"))
    simple_intrest=(n*time*rate)/100
    print("S.I",simple_intrest)
    payble_amount=simple_intrest+n
    print("the total payment is",payble_amount)
    months_1=payble_amount/(time*12)
    accurate_payble=12*months_1
    print("1 year amount payble by user",accurate_payble)
    
    
elif (n>10000)and(n<20001):
    print("please enter a value between 5000 to 10000")     
    time=int(input("time--->"))
    rate=int(input("rate---> 5% to 7.5%"))
    simple_intrest=(n*time*rate)/100
    payble_amount=simple_intrest+n
    print("the total payment is",payble_amount)
elif (n>20001)and(n<100000):
    print("please enter a value between 20001 to 100000")     
    time=float(input("time--->"))
    rate=float(input("rate---> 7.5% to 9%"))
    simple_intrest=(n*time*rate)/100
    payble_amount=simple_intrest+n
    print("the total payment is",payble_amount)
    



else:
    print("please enter valid number for amount.")
    
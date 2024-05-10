#CREATE A PROGRAM TO CHECK WHETHER THE USER ENTER ANY ALPHABET FIND IT VOWEL OR NOT AND ALSO FIND IT CONSONANTS OR NOT

n = str(input("enter the letter----->"))
if ((n=="a" or n=="e" or n=="i" or n=="o" or n=="u")or(n=="A" or n=="E" or n=="I" or n=="O" or n=="U")):
    print ("The entered character is vowel")
elif ((n=="b") or(n=="B")):
     print("The entered character is a consonant")
    
else:
    print("not english alp.")
   
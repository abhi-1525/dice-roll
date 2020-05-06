import random
print("Lets start \n")
a='y'
while(a=='y'):

    roll1=random.randint(1,6)
    roll2=random.randint(1,6)
    print(f"Rolls: {roll1} , {roll2}")
    s=s+1
    if(roll1==6 and roll2==6):
         print("HEYA! U GOT TWO SIXES")
         a='n'
         break
    else:
         continue
print(f"U got two sixes in {s} turns")

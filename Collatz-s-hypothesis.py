c0=int(input("Give me a number:"))
counter=0

while c0 !=1:
    if c0 % 2 ==0: #Number is even
        c0=c0/2
    else: # Number is odd
        c0=3*c0+1
    counter+=1
    print("\n", c0)
else:
    print("steps = ", counter)
        

    
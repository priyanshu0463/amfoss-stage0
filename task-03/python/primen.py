x=int(input("enter the no."))
for i in range(1,x+1):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        print(i,":prime")
        

def sum(num1,**numnbers):
    total = num1    
    if len(numnbers)>0:
        for key in numnbers:
            print key
            total = total +numnbers[key]
    return total

print sum(num1=10,num2=10,num3=20)
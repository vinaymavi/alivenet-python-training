def find_divisble_numbers(n1, n2, r):
    l=[]
    for i in r:
        if (i%7==0) and (i%5!=0):
            l.append(str(i))

    print(','.join(l))
r = range(2000, 3201)

find_divisble_numbers(7,5,r)
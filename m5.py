#list
list=["Apple","Mango","Banana","Pine Apple","Plum"]
for lst in list :
    if lst=='Banana':
        continue
    else:
        print(lst)
#tuples
tpls = ("apple", "banana", "cherry","banana",)
print("Tuples:",tpls)
#Set
st = set(("apple", "banana", "cherry"))
st.add("damson")
st.remove("banana")
print("Set:",st)
print("Length",len(st))


#Dictionary

dct =	dict(apple="green", banana="yellow", cherry="red")
del(dct["banana"])
print("Dictionary:",dct)

a=["s","b","c","d","E"]
b=[1,2,3,4,5,6]

a.append("hh")
print(a[2:])

c="""hello my country is india"""
print(c)
d="hello world"
print(d[1])



q=3
item=434
price=45.45
order="i want {} pieces of items {} for {} mango."
print(order.format(q,item,price))


f=["ghg","djhd","rr","fg"]
print("rr"in f)

i=float(input("enter the first value"))
m=float(input("enter the second value"))
if i>m:
      print("{0} is grateater than {1}".format(i,m))
elif(m>i):
      print("{0} is grateater than {1}".format(m,i))
else:
    print("print both a and b are equal")


for z in range(0,10,2):
      print(z,end=" ")
      print()
      
for x in range(6):
     print(x)
     if x==3:
        break
else:
   print(finally finished")



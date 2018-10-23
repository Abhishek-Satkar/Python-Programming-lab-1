num=int(input("Enter number"))
total=1
if num<1:
 print("invalid")
elif num==0:
 print("1")
else:
 total=num*total
 num=num-1
 print("factorial is", total)

a=[]
print("enter a 5 numbers: ")
for  i in range(5):
    num=int(input("enter number"+str(i+1)))
    a.append(num)
    print(a)
sum=0
for i in a:
    sum=sum+i
print("sum",sum)
average=sum/len(a)

print("average",average)

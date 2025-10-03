a=int (input("a:"))
b=int (input("b:"))
operation= input("add/sub/multi/div: ")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="multi"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("NO")

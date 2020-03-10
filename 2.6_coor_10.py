List = []
n = int(input("what value?"))
for i in range(0,n+1):
    List.append(i)
print(List)
newlist = [i+1 for i in range(n+1)]
print(newlist)
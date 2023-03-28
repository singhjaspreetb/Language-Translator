lis=[]
lis = input("Enter values: ").split()
print(lis)
ans=list(filter(lambda st : len(st) > 3,lis))
print(ans)

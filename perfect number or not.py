n=6
sum=0
for i in range(1,6,1):
  if n%i==0:
    sum=sum+i
print(sum)
if sum==n:
  print("perfect number")
else:
  print("not perfect number")

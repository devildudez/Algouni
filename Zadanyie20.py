participants=int(input("enter the num of ppl"))
a=[]
for i in range(participants):
  s,c,r=input().split()
  s=int(s)
  c=int(c)
  r=int(r)
  a.append((c+r,s))

a.sort(reverse= True)
swim=0
total=0
for i in range(len(a)):
  x,y=i
  swim+=y
  total=max(swim+x,total)

print(total)
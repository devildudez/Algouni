#упражнение 17(2)
rates = [0.9, 0.5, 0.8]
r = list(enumerate(rates))
rates = r.sort(key=lambda x: x[1])
#rates(0, (0, 1,8),(1(1,1.4)))
sm=0
a=[]
for month,rate in enumerate(r):
  sm+=100*(rate[1]**month)
  a.append(rate[0])
print(sm)
print(a)
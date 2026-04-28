#упражнение 17
rates = [1.2, 1.8, 1.4]
r = list(enumerate(rates))
rates = r.sort(key=lambda x: x[1], reverse=True)
#rates(0, (0, 1,8),(1(1,1.4)))
sm=0
a=[]
for month,rate in enumerate(rates):
  sm+=100*(rate[1]**month)
  a.append(rate[0])
print(sm)
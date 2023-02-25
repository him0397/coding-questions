
t = int(input())
for i in range(t):
   x,y = map(int,input().split())
   a=2*x
   b=5*y
   if (a>b):
       print("CHOCOLATE")
   elif(a<b):
       print("CANDY")
   else:
       print("EITHER")
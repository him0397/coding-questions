
t = int(input())
for i in range(t):
   x,y,a=map(int,input().split())
   z = x+y
   if(z==a):
       print("YES")
   else:
       print("NO")
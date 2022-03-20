N=int(input('enter the number sequence needed:'))
i=0
a=0
b=1
while(i<N):
   if(i<=1):
       sum=i
   else:
       sum=a+b
       a=b
       b=sum
   print(sum)
   i=i+1

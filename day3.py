lst=[2,1,5,3,4]
#gift_presented_to
print("Gift presented to:")
print(lst)
n=len(lst)
lst2=[]
if(n%2==0):
  lst2=lst
else:
  a=n
  b=a//2 
  if(b!=2):
    b+=1
  lst2=lst[0:b]
  lst2.append(lst[b+2])
  lst2.append(lst[b])
  lst2.append(lst[b+1])
#gift_received_from
print("Gift received from:")
print(lst2)

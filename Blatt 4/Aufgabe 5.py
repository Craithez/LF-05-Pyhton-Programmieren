import random

def bubblesort(a):
  i = len(a)
  while i!=0:
    j = 0
    while j!=i-1:
      #falls man den Index braucht: "print 'index j:',j"
      if(a[j+1]<a[j]):
        temp = a[j+1]
        a[j+1] =a[j]
        a[j]=temp
      j+=1
    i-=1

#erstelle array mit random values
a=random.sample(range(0,9999),500)
bubblesort(a)
a
print(a)
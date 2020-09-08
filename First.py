#!/usr/bin/env python
# coding: utf-8

# In[1]:


#even_odd

n=int(input("Enter a number:"))
if(n%2==0):
    print("Even")
else:
    print("Odd")


# In[2]:


#Fibonnaci_series
n=20
n1,n2=0,1
count=0

if n<=0:
    print("Not valid")
elif n==1:
    print(n)
    print(n1)
else:
    print("Fibbonaci")
    while count< n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


# In[3]:


#factorial_of_number
n=int(input())
fact=1
while(n>1):
    fact*=n
    n=n-1
print(fact,end=" ")


# In[5]:


#Sum_of_all_even_1-50
n=50
sum1=0
for i in range(1,51):
    if(i%2==0):
        sum1=sum1+i
print(sum1)
        


# In[9]:


#Prime_Number_1-50
lower=1
upper=50
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num,end=" ")


# In[ ]:





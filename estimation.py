#!/usr/bin/env python
# coding: utf-8

# In[14]:


#The exact value of e
import numpy as np
import random
def poisson(lam, n) :
    return n * (lam / n) * (1-lam / n) ** (n-1)
print(1/poisson(1, 10000))


# In[1]:


#The estimation of e with possion
def poisson(lam) :
    el, n, u = np.exp(-lam), 0, np.random.uniform(0, 1)
    pp, fact, pow = el, 1, 1
    if u > pp :
        return False
    return True
x, total = 0, 0
for i in range(0, 10000000) :
    if(poisson(1)) :
        x = x + 1
    total = total + 1
print(total / x)


# In[5]:


#The estimation of e
def poisson(lam, n) :
    ac = 0
    for i in range(0, n) :
        u = np.random.uniform(0, 1)
        if(ac > 1) :
            return False
        if(u < lam/n) :
            ac = ac + 1
    if(ac == 1) :
        return True
    return False
total, x = 0, 0
for i in range(0, 10000) :
    if(poisson(1, 10000)) :
        x = x + 1
    total = total + 1
print(total/x)


# In[6]:


#The estimation of e
def estimate_e(n) :
    total = 0
    for i in range(n) :
        x = 0
        m = 1
        while True :
            new_x = np.random.uniform(0,1)
            if(new_x > x) :
                x = new_x
                m = m + 1
            else :
                total += m
                break
#         print(m)
    return total / n
print(estimate_e(100))


# In[13]:


#The estimation of pi
def estimate_pi(n):
    count = 0
    for i in range(n) :
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if(x**2 + y**2 <= 1) :
            count = count + 1
    return count / n * 4 #pi : 4 = count : n
print(estimate_pi(1000000))


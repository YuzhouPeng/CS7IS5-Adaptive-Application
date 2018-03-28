# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:41:33 2018

@author: vimanyu
"""

import random
import matplotlib.pyplot as plt
import numpy as np

#e = 2.71828

topics = {"music": 0.5, "sports":0.5}
rand_topic = list(np.random.choice(list(topics.keys()), 10, replace=True ))
rand_num = [random.randint(0,9) for i in range(0,10)]

#rand_topic = ["music","music","football","cricket","cricket" ]
#rand_num = [3,2,7,1,0]

def cal_score(t_scr,k):
    if k >= 2 and k<=4:
        a = 0.6
    elif k>=5:
        a = 0.2
    else:
        a=1.5
    score = (pow(a,t_scr) - 1)/(a - 1)
    return score

for i in range(len(rand_topic)):
    l = rand_num[i] 
    topics[rand_topic[i]] = cal_score(topics[rand_topic[i]], l)
    

####

p_score = []

score = 0.5
a = 1.5
for i in range(1,50):
    score = (pow(a,score) - 1)/(a - 1)
    p_score.append(score)
    print(score)

plt.plot(p_score)

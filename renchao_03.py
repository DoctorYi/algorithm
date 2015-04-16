# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
'''人潮最多的時段（ Interval Partitioning Problem ）'''

class Guest():
    '''Guset类，有两个属性，来的时间（正），
    离开的时间（负）'''
    def _init_(self, a, b):
        self.arrival = a
        self.leave = b

'''创建10个Guest对象'''
g = [Guest() for i in xrange(10)]
for i in xrange(10):
    g[i].arrival = int(raw_input('g[%s].arrival : '%i))
    g[i].leave = int(raw_input('g[%s].leave : '%i))



def maximum_guest():
    time = []
    for i in xrange(10):
        time.append(g[i].arrival)
        time.append(-g[i].leave)
    time = sorted(time, key = lambda x: abs(x))
# 请注意sorted函数是返回一个新的序列，并美誉修改原来的time
#sorted在这里是按绝对值排列
    print time
    n, maximum = 0, 0
    for i in xrange(len(time)):
        n = n + 1 if time[i] >= 0 else n-1
        maximum = max(maximum, n)
    print '人潮最多的时段有'+str(maximum)+'人'

maximum_guest()

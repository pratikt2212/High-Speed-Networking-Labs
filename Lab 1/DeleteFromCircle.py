import sys
import os
import random
z = 0
while z != 1 :
    n = int(raw_input("N is the numbers in the circle :"))
    m = int(raw_input("M is the m^th index to be deleted :"))
    k = int(raw_input("K are the numbers remaining in the circle after deletion :"))
    count = 1
    my = [0 for a in range(n)]
    print 'The numbers in the circle are : \n'
    for i in range(0,n) :
        my[i] = i
    print my[0:n]
    y = m
    while n > k :
        if n > y :
            del my[y]
            y = y + m
            n = n - 1
            print my[0:len(my)]
        else:
            del my[y - n ]
            y = y + m - n
            n = n - 1
            print my[0:len(my)]
    print my[0:len(my)]
    z = int(raw_input("Press 1 to end and 0 to repeat again"))






#for i in range(0,k) :
#    print my[i]



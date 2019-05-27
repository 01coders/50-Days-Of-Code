# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:26:38 2019

@author: Parikshith.H
"""

 
a = [10,20,30]
b = [1,2,3]
c = a[0] + b[0]
print(c)
# =============================================================================
# #output:
# 11
# =============================================================================


a = [10,20,30]
b = [1,2,3]
d = a + b  #it concatenates two lists
print(d)
print(type(d))
# =============================================================================
# #output:
# [10, 20, 30, 1, 2, 3]
# <class 'list'>
# =============================================================================
 
e = a*3 #3 times the list a = [10,20,30]
print(e)  
# =============================================================================
# #output:
# [10, 20, 30, 10, 20, 30, 10, 20, 30]
# =============================================================================

 
l = [10,20,30,40]
print(l[1:3]) 
print(l[:2])  
# =============================================================================
# #output:
# [20, 30]
# [10, 20]
# =============================================================================

newl = l[0:4]
print(newl)
print(l)
print(l[::-1])
# =============================================================================
# #output:
# [10, 20, 30, 40]
# [10, 20, 30, 40]
# [40, 30, 20, 10]
# =============================================================================

#program to copy the contents of a listto another list in reverse order
l1 = [10,20,30,40]
l2 = l1[::-1]
print(l1)
print(l2)
# =============================================================================
# #output:
# [10, 20, 30, 40]
# [40, 30, 20, 10]
# =============================================================================

#program to copy half of list in reverse order and other half in same order
l3 = l1[1::-1]
l4 = l1[2:4]
l5 = l3 + l4
print(l5)
# =============================================================================
# #output:
# [20, 10, 30, 40]
# =============================================================================
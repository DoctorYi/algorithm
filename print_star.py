# -*- coding: UTF-8 -*-
'''印出直角三角形'''
''' 多字成行，多行成直角三角形。由細微的東西開始，
一件一件組起來。'''


def print_star(n):
    for i in xrange(n):
        print '*'*(n-i)
print_star(5)

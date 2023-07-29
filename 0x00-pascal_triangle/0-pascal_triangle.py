#!/usr/bin/python3
"""
A function that returns a list of lists of integers representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Returns a list of Integers representing
    the Pascal's triangle
    """
    mylist = [[1]]

    if n <= 0:
        return mylist
    #for i in mylist:
    #    mylist.append([])
    #    mylist[i].append(1)
    for i in range(n - 1):
        tmp =  [0] + mylist[-1] + [0]
        row = []
        for j in range(len(mylist[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        mylist.append(row)
    return mylist

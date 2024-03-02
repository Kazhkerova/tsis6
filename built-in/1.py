from functools import reduce
l=[2,5]
def m(n):
    res=reduce(lambda x,y: x*y,n)
    return res
r=m(l)
print(r)
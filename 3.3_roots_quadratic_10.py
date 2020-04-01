from cmath import*
def roots(a,b,c):
    i = sqrt(b*b - 4*a*c)
    t1 = (-b + i)/(2*a)
    t2 = (-b - i)/(2*a)
    return(t1,t2)
print(roots(5,4,3))
print(roots(-5,-4,-3))
print(roots(1,1,1))
print(roots(-1,-1,-1))




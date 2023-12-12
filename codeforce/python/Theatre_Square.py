
import math
n,m,a=[int(x) for x in input().split()]
x=math.ceil(n/a)
y=math.ceil(m/a)
print(x*y)
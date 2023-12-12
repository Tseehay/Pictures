n=int(input())
count=0

for _ in range(n):
    f=[int(x) for x in input().split()]
    if sum(f)>=2:
        count+=1
print(count)
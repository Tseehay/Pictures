n=int(input())
x=0
for k in range(n):
    s=str(input())
    if "++"==s[:2]:
        x+=1
    elif "--"==s[:2]:
        x-=1
    elif "++"==s[1:]:
        x+=1
    else:
        x-=1
print(x)       
    

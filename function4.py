def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else c>b and c>a:
        return c

sum=max_of_three(1,2,3)
print(sum)


#output:3

def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    if c>b and c>a:
        return c
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
sum=max_of_three(a,b,c)
print(sum)
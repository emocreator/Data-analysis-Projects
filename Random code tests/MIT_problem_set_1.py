x = int(input("Enter number to find if perfect cube: "))
ans = 0
while ans**3 < abs(x):
    ans += 1
if ans**3 != abs(x):
    print("x is not a perfect cube")
else:
    if x < 0:
        ans = -ans
    print("Cube root is "+ str(ans))
    

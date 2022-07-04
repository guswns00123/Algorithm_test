import sys
#snail climing
a,b,c = map(int, sys.stdin.readline().split())

# X * (a - b)= c
# X = c / (a-b)
x =(c - b ) // (a - b)
if (c - b ) % (a - b) == 0:
    print(x)

else:
    print(x+1)
import sys

#break even point

# (C * X) - (A + B * X) > 0
# C * X = A + BX 
# (C - B) * X = A
# X = 1000 / (C- B)

a, b, c = map(int, sys.stdin.readline().split())
print(a // (c-b) + 1 if c > b else -1 )

#runtime err : ans = a // (c-b) 를
#먼저 계산시 c-b = 0일경우 고려 안햇음
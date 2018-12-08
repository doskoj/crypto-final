import sys

e = int(sys.argv[1])
n = int(sys.argv[2])

for i in range(2**38+3, 2**39-1,4):
    if (n%i == 0):
        p = i
        q = n/p

print(p,q)

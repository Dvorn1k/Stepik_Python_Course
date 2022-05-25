#3.5.2
import math
r=float(input())
print(2*math.pi*r)

# 3.5.3
import sys
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end=' ')

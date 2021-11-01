import io
import sys

_INPUT = """\
6
4
2 4 4 3
2
1 2
6
5 5 4 4 3 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  X=list(map(int,input().split()))
  SX=sorted(X)
  l,r=SX[N//2-1],SX[N//2]
  for i in range(N):
    if X[i]<=l: print(r)
    else: print(l)
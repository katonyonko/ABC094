import io
import sys

_INPUT = """\
6
5 3 3
1 2 4
7 3 2
4 5 6
10 7 5
1 2 3 4 6 8 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from bisect import bisect_left
  N,M,X=map(int,input().split())
  A=list(map(int,input().split()))
  idx=bisect_left(A,X)
  print(min(idx, M-idx))
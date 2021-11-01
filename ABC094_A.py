import io
import sys

_INPUT = """\
6
3 5 4
2 2 6
5 3 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,X=map(int,input().split())
  if A<=X<=A+B: print('YES')
  else: print('NO')
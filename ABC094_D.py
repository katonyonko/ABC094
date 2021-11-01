import io
import sys

_INPUT = """\
6
5
6 9 4 2 11
2
100 0
5
2 9 6 5 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  n=int(input())
  a=list(map(int,input().split()))
  a.sort()
  l=a[-1]
  idx=0
  tmp=abs(a[idx]-l/2)
  for i in range(n-1):
    if abs(a[i]-l/2)<tmp:
      idx=i
      tmp=abs(a[i]-l/2)
  print(l, a[idx])
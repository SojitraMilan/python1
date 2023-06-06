def a(*num):
  tot=0
  for i in num:
    tot += i 
  return tot

ans = a(1)
print(ans)
ans = a(1,2,3,4)
print(ans)
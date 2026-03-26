left=0
right=100
while left<right:
  mid=(left+right)//2
  print('your number is',mid)
  ans=input('enter your answer low or high:')

  if ans=='low':
    right=mid
  elif ans=='high':
    left=mid
  else:
    print('your number is',mid)
    break

# 高橋君とホテルイージー
###
# N=5
# K=3
# X=10000
# Y=9000
###
def abc44_a():
  n,k,x,y = [int(input()) for i in range(4)]
  print(k*x+(n-k)*y)

abc44_a()
# n: n+1がブロック総数
# m: ブロック0:1、ブロックn:m
n,m,x=map(int,input().split())
s=sum(int(i)<x for i in input().split())#step数
print(min(s,m-s)) # 左：s、右：m-s

# 1 2 3 4 5 6
# o o o x o o

# G o o X o G
# 1 2 3 4 5 6

# +1されるマスの数はM個
# Aの位置で+1される
# つまり入力値<x（現在地）と置くと
# 左：s、右：m-s:合計mなのでsされた数だけ引けば右側になる
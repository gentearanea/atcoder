N = int(input())
S = []
P = []

for _ in range(N):
   s,p = input().split()
   S.append(s)
   P.append(int(p))
if max(P)>sum(P)/2:
  # リストPの最大値がリストの何番目か調べて
  # 得られたインデックスからシティがどれか調べる
  print(S[P.index(max(P))])
else:
  print("atcoder")
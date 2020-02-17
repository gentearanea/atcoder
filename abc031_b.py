# input
# 300 400
# 3
# 240
# 350
# 480

# output(文字にしてもいいのかな？)
# 60
# 0
# -1

# map（関数, iterable） 関数名を指定するだけで、()は不要
l,w = list(map(int, input().split()))
List = [int(input()) for _ in range(int(input()))]
for x in List:
  print(l-x if l>x else 0 if w>=x else -1)

# if 条件A:
#   処理A
# elif 条件B:
#   処理B
# elif 条件C:
#   処理C
# を
# 処理A if 条件A else 処理B if 条件B else 処理C if 条件V
# と
# 書き換えただけ
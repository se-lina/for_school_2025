# 🔁 FizzBuzz チャレンジ
# for: 繰り返し処理
# range(): 指定回数の繰り返しを作る
# %: 割り算の余り（剰余）を求める
# if / elif / else: 条件で分岐

for i in range(1, 100):  # 1から20まで繰り返す
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # 両方の倍数
    elif i % 3 == 0:
        print("Fizz")      # 3の倍数
    elif i % 5 == 0:
        print("Buzz")      # 5の倍数
    else:
        print(i)           # それ以外の数字

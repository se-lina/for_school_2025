# 🔢 計算クイズ
# int(): 文字を整数に変換する
# if / elif / else: 条件によって分岐する
# 四則演算: + - * /

a = int(input("1つ目の数字を入れてください: "))
b = int(input("2つ目の数字を入れてください: "))
op = input("足し算(+)・引き算(-)・かけ算(*)・割り算(/) のどれをしますか？ ")

if op == "+":
    print("答えは", a + b)
elif op == "-":
    print("答えは", a - b)
elif op == "*":
    print("答えは", a * b)
elif op == "/":
    if b != 0:
        print("答えは", a / b)
    else:
        print("0で割ることはできません")
else:
    print("使えるのは + - * / だけです")

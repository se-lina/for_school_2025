# 🔰 あいさつボット
# input(): ユーザーからの入力を受け取る
# if / elif / else: 条件によって処理を分ける

name = input("あなたの名前は？ ")
time = input("今の時間帯は？（朝・昼・夜）")

if time == "朝":
    print("おはよう、" + name + "さん！")
elif time == "昼":
    print("こんにちは、" + name + "さん！")
elif time == "夜":
    print("こんばんは、" + name + "さん！")
else:
    print("こんにちは、" + name + "さん！")
  

# ✖️ 九九の表
# forの中にforを書くことで、2重ループを作成
# f"{変数}" は文字列に変数を埋め込む方法

for i in range(1, 10):        # 1～9までの行
    for j in range(1, 10):    # 1～9までの列
        print(f"{i} x {j} = {i * j}")

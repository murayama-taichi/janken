import math
p_0 = 1/3
def func():
    bunshi = x-n*p_0
    bunbo = math.sqrt(n*p_0*(1-p_0))
    print(bunshi/bunbo,end=" ")
    if bunshi/bunbo >= 1.64:
        print("H_0")
    else:
        print("H_1")

#全体
x = 182
n = 500
print("全て対象",end=" ")
func()
n = 400
print("相手２を除外",end=" ")
func()

#相手1~5（相手２は勝率0％）
n = 100
x_arr = [25,0,49,68,40]
for i in range(5):
    x = x_arr[i]
    print(f"相手{i+1}",end=" ")
    func()

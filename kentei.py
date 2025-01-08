import math
p_0 = 1/3
def func():
    bunshi = x-n*p_0
    bunbo = math.sqrt(n*p_0*(1-p_0))
    print(bunshi/bunbo)

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
x = 25
print("相手１",end=" ")
func()
x = 0
print("相手２",end=" ")
func()
x = 49
print("相手３",end=" ")
func()
x = 68
print("相手４",end=" ")
func()
x = 40
print("相手５",end=" ")
func()

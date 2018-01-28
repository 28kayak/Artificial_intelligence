#lambda function in python
#those two functions, func1 and func2 should give the identical result.
# 代入する引数a
a = 4
# defを用いてfunc1を作成して下さい
def func1(a):
    result = 2 * pow(a, 2) - 3 * a + 1
    print(result)
    return result


# lambdaを用いてfunc2を作成して下さい
func2 = lambda a: 2 * pow(a, 2) - 3 * a + 1

# 返り値の出力

print("result of Func1 = " + str(func1(a)))
print("result of func2 = "+ str(func2(a)))

#======================================================================
#lambda function with arguments
#substitutions
x = 5
y = 6
z = 2

def func3(x,y,z):
    return x * y + z

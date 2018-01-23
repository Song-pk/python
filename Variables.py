x = 0
print (x)

def TestFunction():
    # global x 를 추가 하면 밑에랑 같은 값이 나온다.
    x = 1
    print (x)

TestFunction()
print (x)
# 처음값과 같은 결과가 나온다

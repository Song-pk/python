print(1 + 2)

print(5 / 3)

#사용자로 부터 값 받기
#변수 활용

name = input("당신의 이름은 무엇입니까?")
print("제 이름은" + name + "입니다.")

# 목록 List Tuple
# 사전 dict - dictionary
# 집합 set

# List []
print("list")
list_a = [1,2,3]
print(list_a)
# print(type([1,2,3]))
# index는 0부터 시작합니다.
print(list_a[0])
print(list_a[1])
print(list_a[2])
# slice
print(list_a[0:2])

list_a.append(4)
print(list_a)

list_a.remove(2)
print(list_a)

list_a.clear()
print(list_a)

# Tuple(1, )
print("tuple")
tuple_a = (1,2,3)
print(tuple_a)
print(type(tuple_a))

# tuple은 한 번 생성 후 내부 값 불가
# tuple_a.append(4) 불가능

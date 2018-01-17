# dict (map)
# key % value

dict_a = {
    "apple" : "a type of fruits",
    "pen" : "a thing to write"
}
print(dict_a)
print(dict_a["apple"])
# edit value
dict_a["pen"] = "something to write"
print(dict_a)

#set set([])
set_a = set([1,2,3])
set_b = set([2,4,6])
print(set_a)
print(set_b)

# 중복 제거
# 집합 - 교집합, 합집합, 차집합, 여집합

print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)

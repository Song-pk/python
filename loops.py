import string

# While Loop

# x = 1
# while True:
#     print("We'll shutdown at count (100,000): " + str(x))
#     if x == 100000:
#         print("Shutdown down....")
#         break
#     x += 1
# print("You have exited the loop.")
# => 1 - 100000 까지 출력


# For loop
# for x in range(0, 9):
#     print("We're on time" + str(x))
# => 1 - 8까지 출력

# Nested loops 중첩된 루프
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(str(x) + '*' + str(y) + '=' + str(x*y))
# => 1 - 10단까지 구구단

#Early exit
# for x in range(3):
#     if x == 2:
#         break
#     else:
#         print(str(x))
# => 0 1 출력


# For..else
# for x in range(3):
#     print(x)
# else:
#     print('Final x = ' + str(x))
# => 0 1 2 Final x = 2


# Strings as an iterable
# string = ("Hello World")
# for x in string:
#     print(x)
# => H e l l o W o r l d

# Lists as an iterable
collection = ['one', 2, 'three']
for x in collection:
    print(x)
# => one 2 three

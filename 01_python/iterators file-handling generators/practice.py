import sys

# f = open("hello.txt", "w")
# s = set(["1", "2", "3", "4", "4", "4", "4", "4", "5", "6", "7", "8", "9"])
# li = list(["\n", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n"])

# f.write("Hello\nthere\n")
# f.writelines(s)
# f.writelines(li)
# f.close()


# f = open("hello.txt", "r")
# # print(f.readline(), end="")
# # str = f.read(10)  # upto 10 chars  unlike read() puts lesser load on memory
# # print(str)

# str = f.readline()
# while str != "":
#     print(str, end="")
#     str = f.readline()

# f.close()

# def recursion_fn(num=0):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * recursion_fn(num-1)

# print(recursion_fn(5))

nums = [x for x in range(1, 1000001)]

# for i in nums:
# print(i)

y = range(1, 1000000001)

print(type(y))
print(sys.getsizeof(nums))
print(sys.getsizeof(y))

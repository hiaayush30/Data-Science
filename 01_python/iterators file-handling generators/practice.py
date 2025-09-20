f = open("hello.txt", "w")
s = set(["1", "2", "3", "4", "4", "4", "4", "4", "5", "6", "7", "8", "9"])
li = list(["\n", "1", "2", "3", "4", "5", "6", "7", "8", "9", "\n"])

f.write("Hello\nthere\n")
f.writelines(s)
f.writelines(li)
f.close()


f = open("hello.txt", "r")
# print(f.readline(), end="")
# str = f.read(10)  # upto 10 chars  unlike read() puts lesser load on memory
# print(str)

str = f.readline()
while str != "":
    print(str, end="")
    str = f.readline()

f.close()

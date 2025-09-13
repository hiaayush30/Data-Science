# strings

# palindrome or not

str = "malayalam"
is_pal = True
for i in range(0, len(str) // 2):
    if str[i] != str[len(str) - 1 - i]:
        is_pal = False
        break

if is_pal:
    print("The string is a palindrome")
else:
    print("not a palindrome")

# split function
str = "Hello there how are you"
li = []
word = ""
for i in str:
    if i != " ":
        word = word + i
    else:
        li.append(word)
        word = ""
li.append(word)  # append the last word when the loop finishes

print(li)

# title function
str = "hi how are you"
# new_str = ""
# for i in str:
#     if str[len(new_str) - 1] in [" ",","]:
#         new_str = new_str + i.upper()
#     else:
#         new_str = new_str + i
# print(new_str)

new_li = []
for i in str.split():
    new_li.append(f"{i[0].upper()}{i[1:]}")

print(" ".join(new_li))

# integer to string function
num = 12345
num_str = "0123456789"
str = ""
while num > 0:
    str = num_str[num % 10] + str
    num = num // 10

print(str)
print(type(str))

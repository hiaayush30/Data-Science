# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

n = int(input("Enter n:"))
x = int(input("Enter x:"))

sum = 1

for i in range(2, n + 1):
    sum = sum + (x**i) / i

print(sum)

# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690.

n = int(input("Enter n:"))
sum = 0
to_add = 2
while n != 0:
    if n == 1:
        print(to_add)
    else:
        print(to_add, end="+")
    sum = sum + to_add
    to_add = int(str(to_add) + "2")
    n = n - 1
print(sum)

# Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                print(i, j, k, l)


# Problem 9: Write a program that will take a decimal number as input and prints out
# the binary equivalent of the number

n = 14
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = int(n / 2)

print(int(binary))

# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers
a = int(input("a:"))
b = int(input("b:"))
lcm = max(a, b)
while lcm % a != 0 or lcm % b != 0:
    lcm = lcm + 1
print("LCM:", lcm)

hcf = min(a, b)
while hcf > 0:
    if a % hcf == 0 and b % hcf == 0:
        break
    hcf = hcf - 1
print("HCF:", hcf)

# Problem 11: Create Short Form from initial character

str = "shorten this string"
short = ""
for i in str.split():
    short = short + i[0].upper()
print(short)

# Problem 12: Append second string in the middle of first string
str1 = "Hellotherewassup"
s = "AMAZNG"
new_str = str1[0 : len(str1) // 2] + s + str1[len(str1) // 2 :]
print(new_str)

# Problem 13:Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
str = "AdjYhsaRE"
lower = ""
upper = ""
for i in str:
    if i.isupper():
        upper = upper + i
    else:
        lower = lower + i
print(lower + upper)

# Problem 14:Take a alphanumeric string input and print the sum and average of the digits
# that appear in the string, ignoring all other characters.
str = "hel123O4every093"
sum = 0
count = 0
for i in str:
    if i.isdigit():
        sum = sum + int(i)
        count = count + 1
print(sum / count)

# Problem 16: Check whether the string is Symmetrical.
s = "madam"
if len(s) % 2 == 0:
    if s[0 : len(s) // 2] == s[len(s) // 2 :]:
        print("symmetrical")
else:
    if s[0 : len(s) // 2] == s[len(str) // 2 + 1 :]:
        print("symmetrical")

# Problem 17: Reverse words in a given String
str = "my name is laxmi"
reversed = str.split()[::-1]
print(" ".join(reversed))

# Problem 18: Find uncommon words from two Strings.
A = "apple banana mango"
B = "banana fruits mango"
arr1 = A.split()
arr2 = B.split()

uncommon_words = []

for i in arr1:
    if i not in arr2:
        if i not in uncommon_words:
            uncommon_words.append(i)
for i in arr2:
    if i not in arr1:
        if i not in uncommon_words:
            uncommon_words.append(i)

print(" ".join(uncommon_words))

# Problem 19: Word location in String.
sentence = "We can learn data science through campusx mentorship program."
word = "campusx"
sen = sentence.split()
index = 0
for i in sentence.split():
    if word == i:
        print("Location of the word is", (index + 1))
        break
    index = index + 1

# Problem 20: Write a program that can remove all the duplicate characters from a string.
# User will provide the input.
str = "jdbchevjkegiuejbshwft"
original = []
for i in str:
    if i not in original:
        original.append(i)
print("".join(original))


for i in range(2000, 3201):
    num = i
    all_even = True
    while num > 0:
        if (num % 10) % 2 != 0:
            all_even = False
            break
        num = num // 10
    if all_even:
        print(i, end=",")

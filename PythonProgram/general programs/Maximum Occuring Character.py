def func(str):
    max = [str[0], str.count(str[0])]
    for i in str:
        if str.count(i) > max[1]:
            max[0] = i
            max[1] = str.count(i)

    return (max)


str = "geeksforgeeks"
print(func(str))
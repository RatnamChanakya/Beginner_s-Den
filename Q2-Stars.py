def pattern(n):
    x = "*"
    for i in range (1, n+1):
        if i % 2 == 0:
            print(x * i)

pattern(10)

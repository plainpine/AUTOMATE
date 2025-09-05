def collatz():
    n = 0
    try:
        input_data = input("整数を入力してください: ")
        n = int(input_data)
    except ValueError:
        print("整数以外は入力しないでください")
        return
    print(n)
    while (n > 1):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
    print()

collatz()
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = input("Введите операцию: ")

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    if b != 0:
        print(a/b)
    else:
        print("Деление на 0!")
else:
    print("Неверная операция!")


def is_number(a: int) -> bool:
    return a // 10 > 0


def is_prime(a: int) -> bool:
    if a < 2: return False

    for i in range(2, a // 2 + 1):
        if a % i == 0: return False
    
    return True


def cnt_odd_digits(a: int) -> int:
    res = 0
    a = abs(a)
    while a > 0:
        res += is_prime(a % 10)
        a //= 10
    return res


def main():
    while True:  # проверка на дурака
        try:
            n = int(input("Введите количество чисел, которые вы хотите ввести: "))
            if n > 0:
                break
            print("N - положительное число!")
        except ValueError:
            print("Ваш ввод некорректен, введите целое число!")
    
    for _ in range(n):
        while True:
            try:
                num = int(input("Введите число: "))
                break
            except ValueError:
                print("Введите целое число!")

        cnt_odd = 0
        if is_number(num):
            cnt_odd = cnt_odd_digits(num)
        print(f"Количество нечетных цифр: {cnt_odd}")


if __name__ == "__main__":
    main()
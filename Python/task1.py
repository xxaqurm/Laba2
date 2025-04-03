def is_prime(a: int) -> bool:
    '''Проверяет, является ли число простым.'''
    if a < 2: return False
    
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0: return False
    
    return True


def main():
    while True:  # проверка на дурака
        try:
            n = int(input("Введите свое N: "))
            break
        except ValueError:
            print("Введенное N должно быть числом!")
    
    deviation = 1
    while True:
        left_val = n - deviation   # ищем простое число слева от N
        right_val = n + deviation  # ищем простое число справа от N
        if is_prime(left_val):
            print(f"N-й член ряда: {n - left_val}")
            break
        elif is_prime(right_val):
            print(f"N-й член ряда: {n - right_val}")
            break
        deviation += 1


if __name__ == "__main__":
    main()

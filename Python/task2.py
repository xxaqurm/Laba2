def drink(N, M):
    full = N
    empty = 0
    total_drunk = 0
    iterations = 0
    steps = []
    
    while True:
        # Шаг 1: Пить все полные бутылки
        if full > 0:
            # Запоминаем состояние до питья
            state_before = []
            for _ in range(full):
                state_before.append("●")
            for _ in range(empty):
                state_before.append("○")
            
            total_drunk += full
            empty += full
            full = 0
            iterations += 1
            
            # Запоминаем состояние после питья
            state_after = []
            for _ in range(full):
                state_after.append("●")
            for _ in range(empty):
                state_after.append("○")
            
            steps.append((iterations, "Выпили все полные", state_before, state_after))
        
        # Проверка условия завершения
        if empty < M:
            break
        
        # Шаг 2: Обмен пустых бутылок на полные
        full = empty // M
        empty %= M
        iterations += 1
        
        # Запоминаем состояние после обмена
        state_after = []
        for _ in range(full):
            state_after.append("●")
        for _ in range(empty):
            state_after.append("○")
        
        steps.append((iterations, f"Обменяли {M} ○ на 1 ●", [], state_after))
    
    return total_drunk, iterations, steps


def display_steps(steps):
    for step in steps:
        print(f"{step[0]} шаг")
        if step[2]:  # Если есть состояние до
            print("До:")
            for i in range(0, len(step[2]), 3):
                print("".join(step[2][i:i+3]))
        print(step[1])
        print("После:")
        for i in range(0, len(step[3]), 3):
            print("".join(step[3][i:i+3]))
        print()


def main():
    N, M = [int(i) for i in input("Введите количество полных бутылок и количество бутылок, которых достаточно для обмена: ").split()]
    print(f"Input: {N} {M}")
    total, iters, steps = drink(N, M)
    print(f"Output: {total} {iters}")
    display_steps(steps)


if __name__ == "__main__":
    main()
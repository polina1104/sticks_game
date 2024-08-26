def start_game():
    total_sticks = int(input("Введите количество палочек в игре: "))
    first_player = input("Введите имя первого игрока: ")
    second_player = input("Введите имя второго игрока: ")

    print(f"\nВыбранное количество палочек в игре: {total_sticks}")
    print(f"Игрок 1: {first_player}")
    print(f"Игрок 2: {second_player}")
    print("Помните правила игры: за один ход можно взять только 1, 2 или 3 палочки. Проигрывает тот, кто берет последнюю. Удачи!")

    current_player = first_player

    while total_sticks > 0:
        print(f"\nСейчас на столе {total_sticks} палочек")
        player_choice = int(input(f"{current_player}, сколько палочек хочешь взять? "))

        if player_choice not in [1, 2, 3]:
            print("Некорректное количество палочек. Введи 1, 2 или 3")
            continue
        if player_choice > total_sticks:
            print("Нельзя взять больше палочек, чем осталось")
            continue

        total_sticks -= player_choice

        if total_sticks == 0:
            print(f"{current_player} взял последнюю палочку и проиграл :(")

        current_player = second_player if current_player == first_player else first_player

start_game()

import random

def guess_number():
    number = random.randint(1, 100)
    tries = 0
    
    print("Привет! Давай поиграем в угадай число. Я загадал число от 1 до 100.")
    
    while True:
        guess = int(input("Угадай число: "))
        tries += 1
        
        if guess < number:
            print("Загаданное число больше")
        elif guess > number:
            print("Загаданное число меньше")
        else:
            print(f"Поздравляю! Ты угадал число за {tries} попыток.")
            break

    play_again = input("Хочешь сыграть еще? (да/нет): ")
    if play_again.lower() == 'да':
        guess_number()
    else:
        print("Спасибо за игру!")
        pass

guess_number()


import random

guesses_made = 0

i = input('Привет! Как тебя зовут?\n')

number = random.randint(1, 100)
print ('Отлично, {0}, я загадал число между 1 и 100. Сможешь угадать?'.format(i))


while guesses_made < 6:
    
    guess = int(input('Введи число: '))
    
    guesses_made += 1

    if guess < number:
        print ('Твое число меньше того, что я загадал.')

    elif guess > number:
        print ('Твое число больше загаданного мной.')

    elif guess == number:
        break

    elif guess == number:
        print ('Ух ты, {0}! Ты угадал мое число, использовав {1} попыток!'.format(i, guesses_made))
else:
    print ('А вот и не угадал! Я загадал число {0}'.format(number))
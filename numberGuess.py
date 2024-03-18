import random

tries = 7

while True:
    randomNumber = random.randint(1, 30)

    print('A random number between 1 and 30 has been generated, try and guess it')
    print('You have ', tries, ' tries, if you´re out of tries you lose')
    print()

    for _ in range(tries):
        try:
            guess = int(input('Your guess: '))
        except ValueError:
            tries -=0
            print('Invalid input! Please enter a number.')
            print()
            continue

        if guess != randomNumber:
            print('You are wrong :(')
            print()
            if guess > randomNumber:
                print('The number ist lower')
            elif guess < randomNumber:
                print('The number is higher')
            tries -= 1
            print('You have ', tries, ' tries left')
            print()
        else:
            print('You are right :)')
            print()
            break

    else:
        print('Out of tries. The correct number was:', randomNumber)
        print('Press enter to continue...')
        print()
        input()

    repeat = input('Type "repeat" to play again or "stop" to end the game: ')

    if repeat.lower() == 'stop':
        break

    if repeat.lower() == 'repeat':
        tries = 7
        continue
      

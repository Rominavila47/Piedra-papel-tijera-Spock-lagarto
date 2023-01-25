import random

options = ('Piedra', 'Papel', 'Tijera', "Spock", "Lagarto")

computer = 0
player = 0
rounds = 1
namePlayer = input("¿Cuál es tu nombre?")
print(f"¡ Excelente {namePlayer} juguemos !")

while True:

    print('°¨¨' * 10)
    print('           ROUND', rounds)
    print('°¨¨' * 10)

    print('Home', computer)
    print(f'{namePlayer}', player)

    Player = input('piedra, papel, tijera  spock o lagarto => ')
    Player = Player.capitalize()

    rounds += 1

    if not Player in options:
        print('esa opcion no es valida')
        continue

    Computer = random.choice(options)

    print(f'{namePlayer} jugaste', Player)
    print('Yo jugué', Computer)

    if Player == Computer:
        print('Empate!')
    elif Player == 'Piedra':
        if Computer == 'Tijera':
            print('Piedra gana a Tijera')
            print('GANASTE!')
            player += 1
        elif Computer == 'Lagarto':
            print('Piedra gana a Lagarto')
            print('GANASTE!')
            player += 1
        elif Computer == 'Papel':
            print('Papel gana a Piedra')
            print('PERDISTE')
            computer += 1
        else:
            print('Spock gana a Piedra')
            print('PERDISTE')
            computer += 1
    elif Player == 'Papel':
        if Computer == 'Piedra':
            print('Papel gana a Piedra')
            print('GANASTE!')
            player += 1
        elif Computer == 'Spock':
            print('Papel gana a Spock')
            print('GANASTE!')
            player += 1
        elif Computer == 'Lagarto':
            print('Lagarto gana a Papel')
            print('PERDISTE')
            computer += 1
        else:
            print('Tijera gana a Papel')
            print('PERDISTE')
            computer += 1
    elif Player == 'Tijera':
        if Computer == 'Papel':
            print('Tijera gana a Papel')
            print('GANASTE!')
            player += 1
        elif Computer == 'Lagarto':
            print('Tijera gana a Lagarto')
            print('GANASTE!')
            player += 1
        elif Computer == 'Piedra':
            print('Piedra gana a Tijera')
            print('PERDISTE')
            computer += 1
        else:
            print('Spock gana a Tijera')
            print('PERDISTE')
            computer += 1
    elif Player == 'Lagarto':
        if Computer == 'Papel':
            print('Lagarto gana a Papel')
            print('GANASTE!')
            player += 1
        elif Computer == 'Spock':
            print('Lagarto gana a Spock')
            print('GANASTE!')
            player += 1
        elif Computer == 'Piedra':
            print('Piedra gana a Lagarto')
            print('PERDISTE')
            computer += 1
        else:
            print('Tijera gana a Lagarto')
            print('PERDISTE')
            computer += 1
    elif Player == 'Spock':
        if Computer == 'Piedra':
            print('Spock gana a Piedra')
            print('GANASTE!')
            player += 1
        elif Computer == 'Tijera':
            print('Spock gana a Tijera')
            print('GANASTE!')
            player += 1
        elif Computer == 'Papel':
            print('Papel gana a Spock')
            print('PERDISTE')
            computer += 1
        else:
            print('Lagarto gana a Spock')
            print('PERDISTE')
            computer += 1

    if computer == 2:
        print('¡¡¡ PERDISTE EL JUEGO !!!')
        break

    if player == 2:
        print('¡¡¡ GANASTE EL JUEGO !!!')
        break


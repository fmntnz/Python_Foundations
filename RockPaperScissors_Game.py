import random

choices = ('piedra', 'papel', 'tijera')

PC_wins = 0
player_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('PC_wins', PC_wins)
    print('player_wins', player_wins)

    player_choice = input('piedra, papel o tijera => ')
    player_choice = player_choice.lower()

    rounds += 1

    if not player_choice in choices:
      print('Entrada incorrecta, por favor escoge piedra, papel o tijera:')
      continue

    PC_choice = random.choice(choices)

    print('player option =>', player_choice)
    print('PC option =>', PC_choice)

    if player_choice == PC_choice:
        print('Empate!, Uff que dificil')
    elif player_choice == 'piedra':
        if PC_choice == 'tijera':
            print('piedra gana a tijera')
            print('player won!')
            print('Animo!, ya casi lo logras')
            player_wins += 1
        else:
            print('Papel gana a piedra')
            print('PC won!')
            print('Animo!, ya casi lo logras')
            PC_wins += 1
    elif player_choice == 'papel':
        if PC_choice == 'piedra':
            print('papel gana a piedra')
            print('player won')
            player_wins += 1
        else:
            print('tijera gana a papel')
            print('PC won!')
            print('Animo!, ya casi lo logras')
            PC_wins += 1
    elif player_choice == 'tijera':
        if PC_choice == 'papel':
            print('tijera gana a papel')
            print('player won!')
            player_wins += 1
        else:
            print('piedra gana a tijera')
            print('PC won!')
            print('Animo!, ya casi lo logras')
            PC_wins += 1

    if PC_wins == 2:
      print('awwwww, Lo lamento... El ganador es la PC')
      break

    if player_wins == 2:
      print('Woow que increible!... GANASTE!')
      break

    
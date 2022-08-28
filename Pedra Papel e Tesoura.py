# Pedra, Papel e Tesoura
# Lucas Anjos | 06/2022

from time import sleep
from random import randint
jogadas = ('PEDRA', 'PAPEL', 'TESOURA')

while True:
    print('\033[34:1m', '-*' * 20, '  JOKENPO  ', '-*' * 20, '\033[m')

    player = int(input('[1] Pedra\n[2] Papel\n[3] Tesoura\n\033[34:1mDigite sua jogada:\033[m '))
    pc = randint(1, 3)

    print('JO...', end='')
    sleep(1)
    print('KEN...', end='')
    sleep(1)
    print('PO!')

    if player == pc:
        print('\033[1:33mEMPATE!')
    elif player == 1 and pc == 2:
        print('\033[1:31mDERROTA!')
    elif player == 2 and pc == 3:
        print('\033[1:31mDERROTA!')
    elif player == 3 and pc == 1:
        print('\033[1:31mDERROTA!')
    elif player == 2 and pc == 1:
        print('\033[1:32mVITÓRIA!')
    elif player == 3 and pc == 2:
        print('\033[1:32mVITÓRIA!')
    elif player == 1 and pc == 3:
        print('\033[1:32mVITÓRIA!')

    print(f'\nVocê jogou {jogadas[player - 1]} e o computador {jogadas[pc - 1]}\033[m')

    choice = int(input('\nDeseja jogar novamente?\n[1] - SIM\n[2] - NÃO\nDigite: '))
    if choice not in (1, 2):
        print('Opção inválida. Tente novamente!')
        break
    if choice == 2:
        print('Obrigado por jogar! :)')
        break



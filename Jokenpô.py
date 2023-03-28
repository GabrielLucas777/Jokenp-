import random
from time import sleep
print('\tJOKENPÔ')
print('\tVamos jogar um jogo, tente ganhar de mim')
while True:
 escolha_p1 = int(input('Pressione [1] Para PEDRA, [2] para TESOURA e [3] Para PAPEL: '))
 print('Estou escolhendo minha opção...')
 sleep(2)
 escolha_pc = (random.randint(1,3))
 print('Feito!')

 if escolha_p1 == 1 and escolha_pc == 2:
     print('Você ganhou, meus parabéns')
 elif escolha_p1 == 2 and escolha_pc == 3:
    print('Você ganhou, meus parabéns')
 elif escolha_p1 == 3 and escolha_pc == 1:
    print('Você ganhou, meus parabéns')
 elif escolha_p1 == escolha_pc:
    print('empatamos')
 else:
    print('Você perdeu, tente novamente.')

    continuacao = input('Deseja continuar? Digite s ou n: ')
    if continuacao == 'n':
       print('Obrigado por jogar!')
       break


    





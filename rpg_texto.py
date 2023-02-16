import time

def dialog():
    time.sleep(4)

def intro(): # Introdução do jogo
    print('"Você acorda em uma caverna escura sem se lembrar de como chegou lá."')
    dialog()
    print('\n"Na sua frente existe uma fogueira, com uma bolsa encostada na parede."')
    dialog()
    print('\n"Você vai até a bolsa para ver o que tem nela."')
    dialog()
    print('\n"Dentro dela tem uma lanterna, pilhas e um martelo."')
    dialog()
    print('\n"A sua frente existe dois caminhos, um para direita e outro para esquerda. Qual caminho você irá seguir?"')

def cap_1_rota_direita(dec_1):
    print('\n"Você decidiu ir pela caminho da direita, é um caminho estreito mas parece ser seguro de prosseguir."')
    dialog()
    print('\n"Com a lanterna "')
def main():
    intro()
    dec_1 = input('\nEscolha um lado para prosseguir (Direita/Esquerda): ')
    if dec_1 == 'Direita':
        cap_1_rota_direita(dec_1)
    #else:
        #cap_1_rota_esquerda(dec_1)
main()
from services import forca


def jogar():
    forca.imprimir_mensagem_abertura()
    palavra_secreta = forca.escolher_palavra_secreta()
    letras_acertadas = forca.inicializar_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0
    letras_faltando = len(letras_acertadas)

    print(letras_acertadas)
    while not acertou and not enforcou:
        chute = forca.pedir_chute()

        if chute in palavra_secreta:
            forca.marcar_chute_correto(chute, letras_acertadas, palavra_secreta)
            letras_faltando = letras_acertadas.count('_')

            if letras_faltando == 0:
                print(f'PARABÉNS!! Você encontrou todas as letras formando a palavra {palavra_secreta}')

        else:
            erros += 1
            print(letras_acertadas)
            print(f'\033[33mAinda falta acertar {letras_faltando} letras.\033[m') 
            print(f'\033[31mVocê ainda tem {7 - erros} tentativas.\033[m')
            forca.desenhar_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        forca.imprimir_mensagem_vencedor()
    else:
        forca.imprimir_mensagem_perdedor(palavra_secreta)

    print('FIM DO JOGO')


if __name__ == '__main__':
    jogar()


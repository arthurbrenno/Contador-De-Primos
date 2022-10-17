import math #Para usar logaritmo natural
import time #Tempo de execução
import os #Limpar o console

def count_primes(limit,precise=False):
    '''
    Uma função que vai realizar todos os cálculos para o programa
    '''
    start_time = time.time()
    if not precise:
        '''
        Aproximação para números maiores
        '''
        return(f'[{limit}]\n'
               f'------------------------------------------------------------------------\n'
               f'N° Primos≅ {round(limit / math.log(limit))}\n' #limite/ln(limite) 
               f'Densidade de primos = {round((1/math.log(limit))*100, 2)}%' #1/ln(limite)
               f'\n------------------------------------------------------------------------' 
               f"\n--- executado em {round(time.time() - start_time, 2)} segundos ---")
    else:
        '''
        Crivo de Eratostenes
        '''
        print("Calculando...")
        list_to_limit = [True] * limit
        list_to_limit[0] = list_to_limit[1] = False
        for _ in range(2, int(limit ** 1 / 2) + 1):
            if list_to_limit[_]:
                for i in range(_ * _, limit, _):
                    list_to_limit[i] = False
        primes = [_ for _ in range(limit) if list_to_limit[_]]
        primes_lenth = len(primes)
        return (f'...\n\n[{limit}]\n'
                f'\nPrimos = {primes}\n\n'
                f'------------------------------------------------------------------------\n'
                f'N° Primos = {primes_lenth}\n'
                f'Densidade de primos = {round(limit/primes_lenth, 2)}%\n'
                f'-----------------------------------------------------------------------'
                f"\n--- executado em {round(time.time() - start_time, 2)} segundos ---")

def main():
    '''
    A função principal para ter uma interface agradável ao usuário
    '''
    print('             || Numeros primos ||                      ')
    print('|||| Saiba quantos números primos existem até o limite ||||\n')
    while True:
        ask = int(input('Digite um limite: '))
        if ask<1000:
            os.system('cls')
            print(count_primes(ask,True))
            break
        else:
            while True:
                print('\nATENÇÃO! Dependendo do tamanho, a opção "precisão" vai levar muito tempo\n')
                print('˅˅˅')
                ask_two = int(input('Você quer que seja preciso(1) ou não(0)? --> '))
                if ask_two==1:
                    ask_two = True
                    os.system('cls')
                    print(count_primes(ask, ask_two))
                    break
                elif ask_two==0:
                    ask_two = False
                    os.system('cls')
                    print(count_primes(ask, ask_two))
                    break
                else:
                    os.system('cls')
                    print('ERRO: Digite um número válido')
                    continue
            break

while True:
    '''
    Checar se o usuário deseja tentar novamente
    '''
    try:
        os.system('cls')
        main()
        ask_three = int(input('\nDigite (1) para tentar de novo ou qualquer coisa para sair -->'))
        if ask_three==1:
            continue
        else:
            break
    except:
        continue
os.system('cls')
exit()
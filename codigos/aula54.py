"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o progama quebre com
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    quant_lista = len(lista)
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('clear')
        lista.append(input('valor: '))
    
    if opcao == 'a':
        o_indice = input('Escolha o índice para apagar: ')
        
        try:
            nume_indice = int(o_indice)
            lista.pop(nume_indice)
        
        except ValueError:
            print('Por favor digite número int.')
        
        except IndexError:
            print('Índice não existe na lista')
        
        except Exception:
            print('Erro desconhecido')
    
    if opcao == 'l':
        os.system('clear')
        if lista == []:
            print('Nada para listar')
        else:
            for indice, nome in enumerate(lista):
                print(indice, nome)
    
    else:
        print('Por favor, escolha i, a ou l.')

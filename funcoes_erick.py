def saudacao():
    print('Olá, digite seu nome: ')
    nome = input()
    while(True):
        print('{}, digite o numero referente a opção desejada:'.format(nome))
        print('\n')
        print('1 - Novo pedido')
        print('2 - Alteração de pedido')
        print('3 - Mais opções')
        op = int(input())
        if(op == 1):
            return novo_pedido()
        elif(op == 2):
            return alteracao_pedido()
        elif (op == 3):
            return mais_opcoes()
        else:
            print('Essa opção não existe')

def novo_pedido():
    print('Essa é a opção novo pedido')

def alteracao_pedido():
    print('O que você deseja alterar?\nDigite o numero referente a opção desejada')
    while(True):
        print('1 - Alterar tamanho')
        print('2 - Alterar sabores')
        print('3 - Alterar extras')
        op = int(input())
        if(op == 1):
            return alterar_tamanho()
        elif(op == 2):
            return alterar_sabores()
        elif(op == 3):
            return alterar_extras()
        else:
            print('Essa opção não existe')

def alterar_tamanho():
    global tamanho
    print('Para qual tamanho deseja alterar? Digite a opção desejada:')
    while(True):
        print('1 - P\n2 - M\n3 - G')
        op = int(input())
        if(op == 1):
            tamanho = 'P'
            return
        elif(op == 2):
            tamanho = 'M'
            return
        elif(op == 3):
            tamanho = 'G'
            return
        else:
            print('Essa opção não existe')


def mais_opcoes():
    print('Essa é a opção mais opções')




menu = {
    1:"AMERICANA",
    2:"APRESUNTADA",
    3:"CROCANTE",
    4:"MILHO",
    5:"MUSSARELA",
    6:"TRADICIONAL",
    10:"ALHO E ÓLEO",
    11:"BACON",
    12:"CALABRESA",
    13:"ESCAROLA",
    14:"FRANGO",
    15:"FRANGO C/ CATUPIRY",
    16:"FRAN-MILHO",
    18:"MARGUERITA",
    19:"MEXICANA",
    20:"NAPOLITANA",
    21:"PAULISTA",
    22:"PORTUGUESA",
    23:"TOSCANA",
    30:"ALICHE"
}


tamanho = ''
recheio_um = ''
recheio_dois = ''
recheio_tres = ''
border = ''
refri = ''
recheio_um = menu[5]
print(menu[1])
print(recheio_um)
# print('Tamanho é : {}'.format(tamanho))
# alterar_tamanho()
# print('Tamanho é : {}'.format(tamanho))

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
    global tamanho
    global cardapio
    global sabores
    print('O que você deseja alterar?\nDigite o numero referente a opção desejada')
    while(True):
        print('1 - Alterar tamanho')
        print('2 - Alterar sabores')
        print('3 - Alterar extras')
        op = int(input())
        if(op == 1):
            return alterar_tamanho()
        elif(op == 2):
            return alterar_sabores(tamanho,cardapio,sabores)
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

def alterar_sabores(tamanho, cardapio,sabores):
    global menu
    if tamanho == 'p':
        print('Escolha o numero referente a novo sabor:/n')
        print(cardapio)
        op = int(input())
        return
    elif tamanho == 'm':
        if len(sabores)==1:
            print('Escolha o numero referente a novo sabor:/n')
            print(cardapio)
            op = int(input())
            return
        elif len(sabores)==2:
            print('Você quer alterar qual sabor:')
            print('1 - {} '.format(menu[sabores[0]]))
            print('2 - {} '.format(menu[sabores[2]]))
            return
def mais_opcoes():
    print('Essa é a opção mais opções')


cardapio = ('NOSSAS OPÇÕES DE SABORES\n\n'
                '01. AMERICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, BACON, CALABRESA, OVOS E CEBOLA\n'
                '02. APRESUNTADA\n'
                'MOLHO DE TOMATE, PRESUNTO E MUSSARELA\n'
                '03. CROCANTE\n'
                'MOLHO DE TOMATE, MUSSARELA (2 CAMADAS), CATUPIRY, BATATA PALHA (DEPOIS DE ASSADA)\n'
                '04. MILHO\n'
                'MOLHO DE TOMATE, MUSSARELA E MILHO\n'
                '05. MUSSARELA\n'
                'MOLHO DE TOMATE E MUSSARELA (2 CAMADAS)\n'
                '06. TRADICIONAL\n'
                'MOLHO DE TOMATE, PRESUNTO, TOMATES E MUSSARELA\n'
                '10. ALHO E OLEO\n'
                'MOLHO DE TOMATE, MUSSARELA, ALHO E AZEITE DE OLIVA\n'
                '11. BACON\n'
                'MOLHO DE TOMATE, MUSSARELA E BACON\n'
                '12. CALABRESA\n'
                'MOLHO DE TOMATE, MUSSARELA E CALABRESA\n'
                '13. ESCAROLA\n'
                'MOLHO DE TOMATE, ESCAROLA (REFOGADA), BACON, ALHO (OPCIONAL) E MUSSARELA\n'
                '14. FRANGO\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO E REFOGADO\n'
                '15. FRANGO C/ CATUPIRY\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO AO MOLHO DE CATUPIRY\n'
                '16. FRAN-MILHO\n'
                'MOLHO DE TOMATE, MUSSARELA, FRANGO DESFIADO AO MOLHO E MILHO\n'
                '18. MARGUERITA\n'
                'MOLHO DE TOMATE, TOMATES, PARMESAO, MANJERICAO, AZEITE DE OLIVA E MUSSARELA\n'
                '19. MEXICANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA RALADA, PIMENTAO VERDE E PIMENTA-CALABRESA\n'
                '20. NAPOLITANA\n'
                'MOLHO DE TOMATE, TOMATES, PROVOLONE E MUSSARELA\n'
                '21. PAULISTA\n'
                'MOLHO DE TOMATE, MUSSARELA, MILHO, ERVILHA, PALMITO E AZEITONAS\n'
                '22. PORTUGUESA\n'
                'MOLHO DE TOMATE, PRESUNTO, MUSSARELA, OVOS, CEBOLA E AZEITONAS\n'
                '23. TOSCANA\n'
                'MOLHO DE TOMATE, MUSSARELA, CALABRESA E OVOS\n'
                '30. ALICHE\n'
                'MOLHO DE TOMATE, MUSSARELA, ALICHE E TOMATES\n')

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
sabores = []

recheio_um = menu[5]
print(menu[1])
print(recheio_um)
# print('Tamanho é : {}'.format(tamanho))
# alterar_tamanho()
# print('Tamanho é : {}'.format(tamanho))

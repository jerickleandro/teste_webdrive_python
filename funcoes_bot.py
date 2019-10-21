def saudacao():
    #Pegar o nome do cliente pela lista do Whatsapp
    nome = input()
    while(True):
        print('{}, digite o numero referente a opção desejada:'.format(nome))
        print('\n')
        print('1 - Novo pedido\n'
        '2 - Alteração de pedido\n'
        '3 - Mais opções')
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
    global tamanho
    while(True):
        print('Qual o tamanho da sua pizza?\n'
              '1.  PEQUENA\n'
              '2.  Mﾃ吋IA\n'
              '3.  GRANDE')
        option = int(input())
        if option == 1:
            tamanho = 'Pequena'
            print(cardapio)
            while(True):
                sabores.append(int(input('Qual o sabor?')))
                #if sabor_um == type(int):
                #    break
                #else:
                #    return ('Opﾃｧﾃ｣o invalida, tente novamente!\n'
                #            'ATENﾃ�ﾃグ! Digite apenas o nﾃｺmero referente ao que deseja.\n')
                break
            break
        elif option == 2:
            tamanho = 'Mﾃｩdia'
            print(cardapio)
            while(True):
                sabor_dois = int(input('Quantos sabores deseja:\n1. Um sabor\n2. Dois sabores'))
                if sabor_dois == 1:
                    sabores.append(int(input('Insira o sabor.')))
                    break
                elif sabor_dois == 2:
                    sabores.append(int(input('Insira o primeiro sabor.')))
                    sabores.append((int(input('Insira o segundo sabor.'))))
                    break
                else:
                    print('Opﾃｧﾃ｣o invalida, tente novamente!\nATENﾃ�ﾃグ! Digite apenas o nﾃｺmero referente ao que desejar.\n')

            break
        elif option == 3:
            tamanho = 'Grande'
            print(cardapio)
            while(True):
                sabor_tres = (int(input('Quantos sabores deseja:\n1. Um sabor\n2. Dois sabores\n3. Trﾃｪs sabores')))
                if sabor_tres == 1:
                    sabores.append(int(input('Insira o sabor.')))
                    break
                elif sabor_tres == 2:
                    sabores.append(int(input('Insira o primeiro sabor.')))
                    sabores.append(int(input('Insira o segundo sabor.')))
                    break
                elif sabor_tres == 3:
                    sabores.append(int(input('Insira o primeiro sabor.')))
                    sabores.append(int(input('Insira o segundo sabor.')))
                    sabores.append(int(input('Insira o terceiro sabor.')))
                    break
                else:
                    print(
                        'Opﾃｧﾃ｣o invalida, tente novamente!\nATENﾃ�ﾃグ! Digite apenas o nﾃｺmero referente ao que desejar.\n')
            break
        else:
            print('Opﾃｧﾃ｣o invalida, tente novamente!\n'
                  'ATENﾃ�ﾃグ! Digite apenas o nﾃｺmero referente ao que desejar.\n')
menu = {
    1:"AMERICANA",
    2:"APRESUNTADA",
    3:"CROCANTE",
    4:"MILHO",
    5:"MUSSARELA",
    6:"TRADICIONAL",
    10:"ALHO E OLEO",
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


def alteracao_pedido():
    print('Essa é a opção alteração pedido')

def mais_opcoes(option):
    borders = ['Catupiry', 'Cheddar', 'Calabresa', 'Queijo', 'Nutela']
    refrigerante = ['Coca-cola', 'Fanta', 'Sprite', 'Kuat', 'Guaraná Antartica']
    if option == 1:
        opt_border = int(input('Deseja adicionar borda?\n(1) SIM\n(2) NÃO'))
        if opt_border == 1:
            print('Escolha o recheio da borda:')
            for i in range(len(borders)):
                print(i,borders[i])
            add_border = int(input())
        more_add = int(input('Deseja adicionar alguma bebida ao seu pedido?\n(1) SIM\n(2) NÃO'))
        if more_add == 1:
            print('Escolha o seu refrigerante:')
            for i in range(len(refrigerante)):
                print(i, refrigerante[i])
            add_refri = int(input())
        return(total_pedido)
    else:
        return(total_pedido)

def total_pedido(total):
    print('Por favor, confirme seu pedido:')
    for i in total:
        print(i)
    answer = int(input('O seu pedido está correto?\n(1) SIM\n(2) NÃO'))
    if answer == 1:
        return(payment)
    else:
        return(alteracao_pedido)

def payment():
    opt_payment = int(input('Qual a forma de pagamento:\n(1) Dinheiro\n(2) Cartão'))
    if opt_payment == 1:
        pay_back = input('Deseja troco?\n(1) SIM\n(2) NÃO')
        if pay_back == 1:
            print('Para quanto deseja o troco?')
            client_money = int(input())
            return(client_money - total_pedido)
    else:
        print('O motoboy levará a máquineta para o pagamento no ato da entrega!')
        print('Agradecemos sua preferência!')

def mais_opcoes():
    print('Mais Opções')
    print('\n')
    while(True):
        print('digite o numero referente a opção desejada:')
        print('\n')
        print('1 - Falar com Atendente Humana')
        print('2 - Voltar para as opções')
        op = int(input())
        if(op == 1):
            print('Essa opção - fala com a Atendente Humana')
            return saudacao()
        elif(op == 2):
            return saudacao()
        else:
            print('Essa opção não é válida')
            return mais_opcoes()
#Vai receber todas as informações do pedido
total = list()

tamanho = ''
sabores = []

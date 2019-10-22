def saudacao():
    # Pegar o nome do cliente pela lista do Whatsapp
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
    def show_cardapio():
        cardapio = open('cardapio.txt', 'r')
        for item in cardapio:
            print(item)
        cardapio.close()
    global tamanho
    while(True):
        print('Qual o tamanho da sua pizza?\n'
              '1.  PEQUENA\n'
              '2.  MÉDIA\n'
              '3.  GRANDE')
        option_size = int(input())
        if option_size == 1:
            tamanho = 'Pequena'
            show_cardapio()
            while (True):
                sabores.append('Informe o numero do sabor desejado:\n')
                if sabor.isnumeric():
                    mais_opcoes(1)
                else:
                    print('Ops! Digite apenas o número do sabor!')
                    sabor = input()
                if len(sabores) == 1:
                    break
        elif option_size == 2:
            tamanho = 'Media'
            show_cardapio()
            while (True):
                for s in range(2):
                    sabor = sabores.append(
                        'Informe o numero do sabor desejado:\n')
                    if sabor.isnumeric():
                        pass
                    else:
                        print('Ops! Digite apenas o número do sabor!')
                        sabor = sabores.append(
                            'Informe o numero do sabor desejado:\n')
                if len(sabores) == 2:
                    mais_opcoes(1)
                    break
        elif option_size == 3:
            tamanho = 'Grande'
            show_cardapio()
            while (True):
                for s in range(3):
                    sabor = sabores.append(
                        'Informe o numero do sabor desejado:\n')
                    if sabor.isnumeric():
                        pass
                    else:
                        print('Ops! Digite apenas o número do sabor!')
                        sabor = sabores.append(
                            'Informe o numero do sabor desejado:\n')


def alteracao_pedido():
    print('Essa é a opção alteração pedido')


def mais_opcoes(option):
    borders = ['Catupiry', 'Cheddar', 'Calabresa', 'Queijo', 'Nutela']
    refrigerante = ['Coca-cola', 'Fanta',
                    'Sprite', 'Kuat', 'Guaraná Antartica']
    if option == 1:
        opt_border = int(input('Deseja adicionar borda?\n(1) SIM\n(2) NÃO'))
        if opt_border == 1:
            print('Escolha o recheio da borda:')
            for i in range(len(borders)):
                print(i, borders[i])
            add_border = int(input())
        more_add = int(
            input('Deseja adicionar alguma bebida ao seu pedido?\n(1) SIM\n(2) NÃO'))
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
    opt_payment = int(
        input('Qual a forma de pagamento:\n(1) Dinheiro\n(2) Cartão'))
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


# Vai receber todas as informações do pedido
total = list()
tamanho = ''
sabores = []
novo_pedido()

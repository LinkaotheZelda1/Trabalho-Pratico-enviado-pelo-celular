
#calculadora

saida = ''

#Função de adição
def adicao(a, b):
    return a + b

#Função de Subtração:
def subtracao(a, b):
    return a - b

#Função de multiplicação:
def multiplicacao(a, b):
    return a * b

#Função de divisão:
def divisao(a,b):
    while a == 0: #aqui eu tive que fazer um while para as duas variáveis caso o valor delas fosse == 0.
        print('Todo número multiplicado por "0" é zero, por favor escolha outro número :b')
        a = float(input('Digite outro número no lugar do primeiro número (variável "A"): '))
    while b == 0:
        print(' Todo número multiplicado por "0" é zero, por favor escolha outro número :b')
        b = float(input('Digite outro número no lugar do segundo número (variável "B"): '))
    return a/b


#Função potência
def potencia(a,b):
    return a**b

#Aqui é onde vai começar o procedimento de qual operação irá ser escolhida:
#Nesse momento, eu tive um problema usando o "or" e atrubuição sendo que o correto seria usar o modo lista.
def calculadora (num1, operacao, num2):
    if operacao in ['+', 'soma', 'adicao']:
        resultado = adicao(num1, num2) #uso da função adição feita lá na linha 6.

    elif operacao in ['-', 'subtracao', 'subtração']:
        resultado = subtracao(num1, num2)

    elif operacao in ['*', 'multiplicação', 'multiplicacao']:
        resultado = multiplicacao(num1, num2)

    elif operacao in ['/', 'divisao', 'divisão']:
        resultado = divisao(num1, num2)

    elif operacao in ['**', 'potencia', 'potência', 'elevado']:
        resultado = potencia(num1, num2)

    else:
        print('Operação inválida, verifique se digitou corretamente.')
    return resultado #TIVE UM PROBLEMA DE 3H TENTANDO RESOLVER ISSO, justamente porque não tinha esse return.


#bem vindo!
print('Você está usando a Calculadora, então execute seus cálculos! \n') #coloquei fora do laço while, para não haver repetição.

# Laço while em que o usuário vai estar voltando todas as vezes para o ínicio após o fim do cálculo:
while saida.lower() != "n":
    try:
# Aqui é a definição das 3 variáveis!
        num1 = float(input('Digite o primeiro número: '))

        operacao = input('Digite o sinal mátemático que será usado: \n(ex: +, -, *, /, **, soma, subtracao, multiplicacao, divisao, ou potencia): ')
        while operacao not in ['+', '-', '*', '/', '**', 'soma', 'subtracao', 'multiplicacao', 'divisao', 'potencia']:
            print('\n Você colocou uma função matemática que está fora da lista, corrija para terminarmos o cálculo. \n')
            operacao = input('Digite o sinal mátemático que será usado: \n(ex: +, -, *, /, **, soma, subtracao, multiplicacao, divisao, ou potencia): ')

        num2 = float(input('Digite o segundo número: '))
#Repare que eu coloquei a função para ser colocada no meio e não no final. Faz muito mais sentido, até porque ninguém coloca a operação por último em uma calculadora.

        resultado = calculadora(num1, operacao, num2)
        print('O resultado da operação é: ', resultado)

        saida_da_calculadora = input('Deseja continuar? (S/N): ').strip().lower() #colocar strip e lower, para não dar erro de espaços e maiúscula.
        if saida_da_calculadora in ["n","não", 'nao']:
            break #qualquer entrada que não seja "n", vai reiniciar os cálculos novamente.

    except ValueError: #concordo que não sei usar o "try, except" ainda. Tive que fazer um "while not in" em OPERACAO porque o except não estava ativando nele.
            print("Por favor, digite somente números. Leia atentamente e certifique-se de digitar números corretamente.")


print('Obrigado por usar a calculadora! \n by Wesley Alves Prates')

#OBS: também tive o entusiasmo de colocar uma função de potência / **
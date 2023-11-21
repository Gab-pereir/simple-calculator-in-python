def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

# Função principal
def calculadora():
    print("Calculadora Simples")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    escolha = input("Escolha a operação (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(f"A soma é: {soma(num1, num2)}")
    elif escolha == '2':
        print(f"A subtração é: {subtracao(num1, num2)}")
    elif escolha == '3':
        print(f"A multiplicação é: {multiplicacao(num1, num2)}")
    elif escolha == '4':
        print(f"A divisão é: {divisao(num1, num2)}")
    else:
        print("Escolha inválida. Por favor, escolha uma operação válida.")

# Chama a função principal
calculadora()

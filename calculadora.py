def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculadora():
    print("Selecione a operação:")
    print("1.Soma")
    print("2.Subtração")
    print("3.Multiplicação")
    print("4.Divisão")

    while True:
        escolha = input("Digite sua escolha(1/2/3/4): ")

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                continue

            if escolha == '1':
                print(num1, "+", num2, "=", somar(num1, num2))

            elif escolha == '2':
                print(num1, "-", num2, "=", subtrair(num1, num2))

            elif escolha == '3':
                print(num1, "*", num2, "=", multiplicar(num1, num2))

            elif escolha == '4':
                print(num1, "/", num2, "=", dividir(num1, num2))
            
            nova_calculo = input("Deseja fazer outro calculo? (sim/não): ")
            if nova_calculo.lower() != 'sim':
                break
        else:
            print("Entrada Inválida")

if __name__ == "__main__":
    calculadora() 
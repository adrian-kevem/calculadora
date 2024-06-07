import os

def menu():
    print("\nCALCULADORA PYTHON")
    print("==================")
    print("1 - SOMA")
    print("2 - SUBTRAÇÃO")
    print("3 - MULTIPLICAÇÃO")
    print("4 - DIVISÃO")
    print("5 - POTENCIAÇÃO")
    print("6 - RADICIAÇÃO")
    try:
        opcao1 = int(input(">>>>> Digite uma opção: "))
        while ((opcao1 < 0) or (opcao1 > 6)):
            opcao1 = int(input(">>>>> Digite uma opção válida: "))
    except Exception:
        print("Entrada inválida!")
        menu()
    return opcao1

def soma():
    print("SOMA")
    print("====")
    a = float(input(">>>>> Digite o valor da primeira parcela: "))
    b = float(input(">>>>> Digite o valor da segunda parcela: "))
    result = a + b
    print(f"Resultado: {result}")

def sub():
    print("SUBTRAÇÃO")
    print("=========")
    a = float(input(">>>>> Digite o valor do minuendo: "))
    b = float(input(">>>>> Digite o valor do subtraendo: "))
    result = a - b
    print(f"Resultado: {result}")

def mult():
    print("MULTIPLICAÇÃO")
    print("=============")
    a = float(input(">>>>> Digite o valor do primeiro fator: "))
    b = float(input(">>>>> Digite o valor do segundo fator: "))
    result = a * b
    print(f"Resultado: {result}")

def div():
    print("DIVISÃO")
    print("=======")
    a = float(input(">>>>> Digite o valor do dividendo: "))
    b = float(input(">>>>> Digite o valor do divisor: "))
    result = a / b
    print(f"Resultado: {result}")

def pot():
    print("POTENCIAÇÃO")
    print("===========")
    a = float(input(">>>>> Digite o valor da base: "))
    b = float(input(">>>>> Digite o valor do expoente: "))
    result = a ** b
    print(f"Resultado: {result}")

def rad():
    print("RADICIAÇÃO")
    print("==========")
    a = float(input(">>>>> Digite o valor do radicando: "))
    b = float(input(">>>>> Digite o valor do índice: "))
    result = (a ** (1/b))
    print(f"Resultado: {result}")

if __name__ == "__main__":
    opcao2 = 1
    while opcao2 == 1:
        os.system("cls")
        opcao1 = menu()
        os.system("cls")
        if opcao1 == 1:
            soma()
        elif opcao1 == 2:
            sub()
        elif opcao1 == 3:
            mult()
        elif opcao1 == 4:
            div()
        elif opcao1 == 5:
            pot()
        elif opcao1 == 6:
            rad()
        else:
            print("Opção inválida!")
        try:
            opcao2 = int(input(">>>>> Digite '1' para continuar realizando operações e '2' para sair: "))
            while ((opcao2 < 0) or (opcao2 > 2)):
                opcao2 = int(input(">>>>> Digite uma opção válida: "))
            print("Saindo...")
        except Exception:
            print("Entrada inválida! Saindo...")
            opcao2 = 2

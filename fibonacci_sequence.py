def fibonacci_sequence(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_pertence(numero_inserido):
    fibonacci = fibonacci_sequence(numero_inserido)
    if numero_inserido in fibonacci:
        print(f"O número {numero_inserido} pertence à sequência de Fibonacci.")
        return
    else:
        print(f"O número {numero_inserido} não pertence à sequência de Fibonacci.")
        return


numero_inserido = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
verifica_pertence(numero_inserido)

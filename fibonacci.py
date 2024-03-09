def fibonacci_sequencia(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
44

numero = int(input("Informe um número: "))
sequencia = fibonacci_sequencia(numero)
verifica_pertence(numero, sequencia)
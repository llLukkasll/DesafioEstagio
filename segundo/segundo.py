# Define a função que calcula a sequência de Fibonacci
def fibonacci(n):
    # Inicia a sequência com os valores 0 e 1
    fib = [0, 1]
    # Loop para calcular os próximos valores da sequência
    while fib[-1] < n:
        next_fib = fib[-1] + fib[-2]
        fib.append(next_fib)
    # Verifica se o número informado pertence à sequência
    if n in fib:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")
    # Retorna a sequência calculada
    return fib

# Solicita ao usuário que informe um número
n = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Chama a função fibonacci com o número informado e exibe a sequência calculada
fib = fibonacci(n)
print(f"Sequência de Fibonacci até o valor mais próximo (maior ou igual) a {n}:")
print(fib)

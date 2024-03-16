def fibonacci(numero):
    a, b = 0, 1
    sequencia = [a,b]

    while b < numero:
        a, b = b, a + b
        sequencia.append(b) #adicionar a lista

        if b == numero:
            return sequencia
    return sequencia[:-1] # remover último número, caso contrário, a lista vai mostrar o próximo


numero = int(input("Digite um número: "))
sequencia = fibonacci(numero)

if numero in sequencia:
    print(f"O número {numero} pertence à sequência.")

else:
    print(f"O número {numero} não pertence à sequência.")
    
print(f'Sequência fornecida: {sequencia}')

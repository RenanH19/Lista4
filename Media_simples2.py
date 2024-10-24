def calcular_media(tamanho_sequencia):
    tamanho_sequencia = int(input("Digite o tamanho da sequência para calcular a média"))
    media = 0
    for i in range(tamanho_sequencia):
        valor = float(input(f"Digite o valor {i + 1}: "))
        media += valor

    return media/tamanho_sequencia

print(calcular_media(5))


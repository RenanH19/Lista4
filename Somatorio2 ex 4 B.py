def soma_sequencia2():
    somaX = 0
    for x in range(1,4):
        somaY = 0
        for y in range(1,3):
            somaY = x * y - 5
        somaX += somaY
    return somaX

print(soma_sequencia2())
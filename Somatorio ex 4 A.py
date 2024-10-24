def soma_sequencia_2():
    somaX = 0
    for x in range(2,6):
        somaY = 0
        for y in range(2,4):
            somaY += (x+y)**2
        somaX += somaY
    return somaX

print (soma_sequencia_2())
    

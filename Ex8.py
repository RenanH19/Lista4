import random
def sorteia():
    lista = []
    for i in range(6):
        lista.append(random.randint(1,100))
    return lista

def somaPar():
    soma = 0
    lista = sorteia()
    print ({i+1:lista[i] for i in range(len(lista))})
    for i in lista:
        if i % 2 == 0:
            soma += i
            print(f'número somado {i} \n')
    return soma

print(somaPar())
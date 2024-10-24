def inverter_ordem(dicionario):
    lista = ['a', 'b', 'c', 'd', 'e']
    invertido = {}
    for i in range(len(lista)):
        invertido[lista[i]] = dicionario[lista[-1-i]]
    return invertido

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(inverter_ordem(dicionario))
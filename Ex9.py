def lerCaractere(palavra):
    lista =[]
    for i in palavra:
        if i.isalpha() and i not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            lista.append(i)
    print(set(lista))
            

lerCaractere(['a', 'b', 'c', 'd', 'e', 'f'])
# lerCaractere()
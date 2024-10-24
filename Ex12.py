listaEnquete = []

while True:
    i = int(input("Digite 1-Python\n 2-C++\n 3-Java\n 4-Rust\n 5-C#\n 6-Outro \n 0-finalizar enquete\n"))
    if i == 0:
        break
    elif i == 1:
        listaEnquete.append("Python")
    elif i == 2:
        listaEnquete.append("C++")
    elif i == 3:
        listaEnquete.append("Java")
    elif i == 4:
        listaEnquete.append("Rust")
    elif i == 5:
        listaEnquete.append("C#")
    elif i == 6:
        listaEnquete.append("Outro")
    else:
        print("Opção inválida")
    
porcentagem = {'Python': 0, 'C++': 0, 'Java': 0, 'Rust': 0, 'C#': 0, 'Outro': 0}
contador = 0
for i in (listaEnquete):
    if i in porcentagem:
        porcentagem[i] += 1
    contador += 1

print(porcentagem)

print(f"Linguagem     Votos     %    \n ------------------------------\n Python:      {porcentagem['Python']}      {porcentagem['Python']/contador*100:.2f}%\n C++:         {porcentagem['C++']}      {porcentagem['C++']/contador*100:.2f}%\n Java:        {porcentagem['Java']}      {porcentagem['Java']/contador*100:.2f}%\n Rust:        {porcentagem['Rust']}      {porcentagem['Rust']/contador*100:.2f}%\n C#:          {porcentagem['C#']}      {porcentagem['C#']/contador*100:.2f}%\n Outro:       {porcentagem['Outro']}      {porcentagem['Outro']/contador*100:.2f}%\n")

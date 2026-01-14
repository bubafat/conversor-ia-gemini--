import os

lista = []
for i in range(5):
    item = str(input("Digite algo: "))
    lista.append(item)

while True:
    os.system('cls')
    print("Itens na lista:")
    for i in lista:
        print("-", i)
    print("__________________________")
    item = str(input("Digite 'sair' para encerrar): "))
    if item.lower() == 'sair':
        break
    lista.append(item)

for i in range(5):
    item = str(input("Digite algo"))

#os.name: Uma forma inteligente de saber se o sistema é Windows ('nt') ou não, para usar o comando de limpar tela correto.

#.lower(): Garante que se o usuário digitar "SAIR" ou "Sair", o programa entenda o comando.

#lista.sort(): Adicionei dentro do loop para que, toda vez que você inserir algo novo, a lista se auto-organize
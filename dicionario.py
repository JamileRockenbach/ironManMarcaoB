import os
os.system("cls")

telefones = { 
    'João': '9999-9999',
    'Maria': '9657-9289',
    'Pedro': '1723-2823',
    'Ana': '7263-0283' 
}
telefones["Lucas"] = "5678-9012" 
busca = input("Digite o nome que deseja buscar: ")
print(telefones.get(busca, "Nome não encontrado!"))


nome = input("Informe o seu nome: ")
idade = input("Informe sua idade: ")

print("Olá", nome)
print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="_")
print(nome, idade, sep="_", end="...\n")

# Por padrão, o sep é atribuido como um caracter vazio " " e o end é atribuido apenas uma quebra de linha "\n"
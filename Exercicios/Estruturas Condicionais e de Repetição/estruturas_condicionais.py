MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade, pode tirar a CNH!")
else:
    print("Menor de idade, não pode tirar a CNH!")



if idade >= 18:
    print("Maior de idade, pode tirar a CNH!")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não as práticas")
else:
    print("Menor de idade, não pode tirar a CNH!")
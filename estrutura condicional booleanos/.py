qtde_faltas = int(input("digite a quantidade de faltas:  "))
media_final = int(input("digite a média final:  "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else:
    print("aluno reprovado! ")
    
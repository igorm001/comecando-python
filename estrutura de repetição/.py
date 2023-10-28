#estrutura de repetição em python: while e for
#em um a estrutura de repetição sempre há uma estrutura decisão, pois a repetição de um trcho de sempre está associada a uma condição. ou seja, 
#um bloco de comandos será executado repetidas vezes, até que uma condigção não seja mais satisfeita

numero = int
while numero != 0:

    numero = int(input("digite um numero:  "))


    if numero % 2 == 0:
        print("numero par!")

    else:
        print("numero impar!")

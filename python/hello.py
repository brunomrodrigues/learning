
print("Jogo da Adivinhacao")


numero_secreto                  = 42
tentativa                       = 1

print("*******************")
total_tentativas_desejadas_str  = input("Digite quantas tentativas você deseja utilizar:")
total_tentativas_desejadas      = int(total_tentativas_desejadas_str)
print("*******************")
print(total_tentativas_desejadas)

while(tentativa <= total_tentativas_desejadas):
    
    print("Tentativa número", tentativa)
    chute_str               = input("Digite o seu numero:")
    chute                   = int(chute_str)
    numero_maior_que_chute  = chute > numero_secreto
    numero_menor_que_chute  = chute < numero_secreto
    acertou                 = numero_secreto == chute

    if(acertou):
        print("Você acertou!")
    else:
        if(numero_maior_que_chute):
            print("Seu número é maior que o número secreto!")
        elif(numero_menor_que_chute):
            print("Seu número é menor que o número secreto!")

    tentativa                  = tentativa + 1

print("Fim do Jogo!!!!")

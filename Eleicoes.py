title = "Gerenciador de eleicoes"
print("{:*^80}".format(title))
votoPartidoA = 0
votoPartidoB = 0
senha = 1234
condicaoAdmin = True
qtVotantes = int(input("Digite a Quantidade de votantes? "))
titulo= 'Votos'
print('{:=^80}'.format(titulo))
print("Partido A - Opcao [1]")
print("Partido B - Opcao [2]")

for i in range(qtVotantes):
    voto = int(input("Informe o Partido [1 - 2]: "))
    if voto == 1:
        votoPartidoA += 1
    elif voto == 2:
        votoPartidoB += 1
    else:
        print("Voto Nulo")

while(condicaoAdmin):
    admin = int(input("Deseja ver o vencedor das Eleicoes\nSe sim entre como Admin inserindo [9]: "))
    if admin == 9:
        while(True):
            password = int(input("Digite a Senha: "))
            if password == senha:
                print("Seja benvindo, Sr.Admin")
                if votoPartidoA > votoPartidoB:
                    percentagem = 100*votoPartidoA/qtVotantes
                    print("Total de votos: {}".format(qtVotantes))
                    print("O partido A venceu as Eleicoes.\nCom {}% dos votos\nObtendo um total de {} votos"
                          .format(percentagem,votoPartidoA))
                    condicaoAdmin=False
                    break
                
                elif votoPartidoA == votoPartidoB:
                    print("Total de votos: {}".format(qtVotantes))
                    print("Há um empate entre os partidos A e B")
                    condicaoAdmin=False
                    break

                else:
                    percentagem = 100*votoPartidoB/qtVotantes
                    print("Total de votos: {}".format(qtVotantes))
                    print("O partido B venceu as Eleicoes.\nCom {}% dos votos\nObtendo um total de {} votos"
                          .format(percentagem,votoPartidoB))
                    condicaoAdmin=False
                    break

            else:
                print("Senha Incorreta")
                continue
    else:
        print("Valor incorreto!")
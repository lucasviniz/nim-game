############CODIGO-TESTE#############
def multiplo(n, m):
    m=m+1
    u=0
    while n!=u and u<n:
        u=m+u
    if u==n:
        return True
    else:
        return False

def computador_escolhe_jogada(n, m):
    x=1
    b=True
    while x<m and b:
        if multiplo(n-x, m)==True:
            b=False
        else:
            x=x+1
    if multiplo(n-x, m)==True:
        return x
    else:
        return m

def  usuario_escolhe_jogada(n, m):
    er=0
    while er<1:
        jogada=int(input("Quantas peças deseja retirar ?"))
        if jogada<=m and n>0 and jogada>0:
            er=1
            return jogada
        else:
            print("Oops! Jogada inválida! Tente de novo.")

def partida():
        n=int(input("Quantas peças ? "))
        a=0
        result=0
        m=int(input("Limite de peças por jogada? "))
        j=0

        if multiplo(n, m)==True:
            print("você começa")
            valorUser=usuario_escolhe_jogada(n, m)
            n=n-valorUser
            print("Você retirou",valorUser,"peças")
            if n<=0:
                result=1
            else:
                print("Agora restam",n,"peças no tabuleiro.")
            j=1
        else:
            print("Computador começa!")
            varComp=computador_escolhe_jogada(n, m)
            n=n-varComp
            print("O computador tirou",varComp,"peça.")
            if n<=0:
                result=2
            else:
                print("Agora restam",n,"peças no tabuleiro.")
            j=2

        while result!=1 and result!=2:
            if a<1:
                if j==2:
                    valorUser=usuario_escolhe_jogada(n, m)
                    n=n-valorUser
                    print("Você retirou",valorUser,"peças")
                    if n<=0:
                        result=1
                        break
                    print("Agora restam",n,"peças no tabuleiro.")
                    j=1
                if j==1:
                    varComp=computador_escolhe_jogada(n, m)
                    n=n-varComp
                    print("O computador tirou",varComp,"peça.")
                    if n<=0:
                        result=2
                        break
                    print("Agora restam",n,"peças no tabuleiro.")
                    j=2
        return result

def campeonato():
    escolha_partida=int(input("Bem-vindo ao jogo do NIM! Escolha:\n \n1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    repeat=3
    placar1=0
    placar2=0
    h=0
    while repeat>0:
        if escolha_partida==1:
            result=partida()
            repeat=0
        if escolha_partida==2:
            h=h+1
            print("\n**** Rodada ",h,"****")
            result=partida()

        if result==1:
            placar1=placar1+1
            print("O jogador ganhou!")
        if result==2:
            placar2=placar2+1
            print("O computador ganhou!")
        repeat=repeat-1
        if repeat==0:
            print("**** Final do campeonato! ****")
            print("Placar: Você",placar1,"X",placar2,"Computador")

campeonato()




############CODIGO-TESTE#############
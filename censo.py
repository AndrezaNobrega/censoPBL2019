regioes = list()
leitor= open('tecnicosIBGE.txt','r')
regioes = (leitor.readlines)
print(regioes[3])



'''def. serve para definir funções onde terá uma sequencia de comandos, e quando você precisar dessas
sequência em alguma parte do programa basta chama-la que ela vai executar a função que você definiu.'''


#how to create a menu in python
'''
ans=0
while ans !=4:
    print ('1.Importar informações das regiões 2.Cadastrar técnicos 3.Pesquisar técnico 4.Importar informações das pesquisas')
    ans=input("O que deseja fazer?")
    if ans=="1":
        print("\nA seguir, serão importadas as informações de regiões")
        info_regioes=open('regioes.txt', 'w')
        texto=0
        info_regioes.write(texto)
        info_regioes()
        info_regioes.close()


    elif ans=="2":
        print("\n Cadastrando técnicos...")
    elif ans=="3":
        print("\n Pesquisa de técnico foi selecionada!")
    elif ans=="4":
        print("\n Importando informações das pesquisas")
        #começar pesquisa
    else:
        print("\n Tente outra opção!")
'''

'''matriz = [[5, 10, 20],[2, 4, 6],[10, 25, 50]]
print "Exemplo de matriz de ordem 3x3:\n"
print matriz
print "1ª linha, 1ª coluna:", matriz[0][0]
print "1ª linha, 2ª coluna:", matriz[0][1]
print "1ª linha, 3ª coluna:", matriz[0][2]
print "2ª linha, 1ª coluna:", matriz[1][0]
print "2ª linha, 2ª coluna:", matriz[1][1]
print "2ª linha, 3ª coluna:", matriz[1][2]
print "3ª linha, 1ª coluna:", matriz[2][0]
print "3ª linha, 2ª coluna:", matriz[2][1]
print "3ª linha, 3ª coluna:", matriz[2][2]
'''


'''
# função para cadastrar os funcionários no programa
def ibge ():
    nome=str(input('Digite o seu nome: '))
    matricula=int(input('Digite a sua matrícula:'))
    sexo=int(input('1.Masculino \n 2.Feminino'))
    print('Olá,', nome,'!')

ibge()
ibge()
ibge()
ibge()

'''''

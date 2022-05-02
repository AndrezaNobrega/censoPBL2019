



'''Esse bloco é o menu do programa, onde o usuário irá escolher a função utilizada'''

res=0
while res !=4:
    print (' 1.Importar informações das regiões\n 2.Cadastrar técnicos\n 3.Pesquisar técnico\n 4.Importar informações das pesquisas')
    res=input(" O que deseja fazer?")
    
    
    if res=="1":
        print('\nA seguir, serão importadas as informações de regiões')
    if res =="2":
        print('\n Cadastrando técnicos...')
    elif res=="3":
        print('\n Pesquisa de técnico foi selecionada!')
        
#A função tecnicos é usada para pesquisar a matrícula do técnico
# - lista: é usada para criar a lista 
# -dadostec: irá receber as informações dos técnicos
# -o for coluna é usado para controlar as colunas
#-o subvetor é usado para dividir as informações do arquivo com o ";"
#- por fim, tem-se uma condicional que compara se a informação dada existe dentro do arquivo importado '''
     
        def tecnicos(arq_tecnico,matricula):
            lista = list()
            dadostec = open(arq_tecnico,'r')
            lista =  (dadostec.readlines())
            for coluna in range(200):
                linha=(lista[coluna])
                subvetor= (linha.split(';'))
                if subvetor[0]==matricula:
                    X=('{} foi encontrado!' .format(matricula))
                    break
                else:
                    X=('Não foi encontrado')
            return X
        tecnico_pesq = input('Qual é a sua matrícula?')
        print (tecnicos('tecnicosIBGE.txt',tecnico_pesq))

        

    elif res=="4":
        print('\n Importando informações das pesquisas')
        #começar pesquisa
    else:
         print("\n Tente outra opção!")

'''A função tecnicos é usada para pesquisar a matrícula do técnico
 - lista: é usada para criar a lista 
 -dadostec: irá receber as informações dos técnicos
 -o for coluna é usado para controlar as colunas
 -o subvetor é usado para dividir as informações do arquivo com o ";"
 - por fim, tem-se uma condicional que compara se a informação dada existe dentro do arquivo importado '''

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
tecnico_pesq = input('Qual é o seu nome?')
print (tecnicos('tecnicosIBGE.txt',tecnico_pesq))

def tecnicos(arq_tecnico,matricula):
    lista = list()
    dadostec = open(arq_tecnico,'r')
    lista =  (dadostec.readlines())
    for coluna in range(200):
        linha=(lista[coluna])
        subvetor= (linha.split(';'))
        if subvetor[0]==matricula:
            X=('{} foi encontrado!' .format(matricula))
            return X


tecnico_pesq = input('Qual é o seu nome?')
print (tecnicos('tecnicosIBGE.txt',tecnico_pesq))

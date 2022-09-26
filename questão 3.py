Luiz=Inácio=Lula=Da_Silva=Nulo=Branco=0
while True:
    x = int(input('Insira seu voto. 1 - Luiz, 2 - Inácio, 3 - Lula e 4 - Da Silva. Selecione 5 para anular e 6 para votar em branco: '))
    if x==1:
        Luiz+=1
    elif x==2:
        Inácio+=1
    elif x==3:
        Lula+=1
    elif x==4:
        Da_Silva+=1
    elif x==5:
        Nulo+=1
    elif x==6:
        Branco+=1
    elif x==0:
        print('Encerramento de votações.')
        break
perc1 = round(Nulo*100/(Luiz+Inácio+Lula+Da_Silva+Nulo+Branco),2)
perc2 = round(Branco*100/(Luiz+Inácio+Lula+Da_Silva+Nulo+Branco),2)
print ('O total de votos para cada candidato foi:','Luiz: {}'.format(Luiz),'Inácio: {}'.format(Inácio),'Lula: {}'.format(Lula), 'Da Silva: {}'.format(Da_Silva), sep='\n')
print ('O total de votos nulos foi de {}'.format (Nulo))
print ('O total de votos brancos foi de {}'.format(Branco))
print ('A percentagem de votos nulos foi de {}%'.format(perc1))
print ('A percentagem de votos brancos foi de {}%'.format(perc2))
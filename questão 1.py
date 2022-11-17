a=b=c=d=n=0
while n>=0:
    n = float(input('Insira um número: '))
    if 0<=n<=25: 
        a+=1
    elif 26<=n<=50:
        b+=1
    elif 51<=n<=75:
        c+=1
    elif 76<=n<=100:
        d+=1
    elif n>100:
        print('Valor inválido.')
    else:
        print('Valor negativo. Fim da contagem.')
print ('A quantidade de números inseridos nos intervalos:\n',f'[0-25] = {a}.\n', f'[26-50] = {b}.\n', f'[51-75] = {c}.\n', f'[76-100] = {d}.\n')

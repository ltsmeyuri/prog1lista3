valor_a_ser_pago=0
while True:
    x = int(input('Insira o código do produto: '))
    a = int(input('Insira a qtde desse produto: '))
    s = input('Deseja continuar? (S/N): ')
    if x ==100:
        valor_a_ser_pago+=a*1.2
    if x==101:
        valor_a_ser_pago+=a*1.3
    if x==102:
        valor_a_ser_pago+=a*1.5
    if x==103:
        valor_a_ser_pago+=a*1.2
    if x==104:
        valor_a_ser_pago+=a*1.3
    if x==105:
        valor_a_ser_pago+=a
    if s in 'Nn':
        break
print('Valor total é de R$:{}'.format(valor_a_ser_pago))        
lista1 = []
lista2 = []
lista3 = []
lista4 = []

while True:
    x = (int(input("Digite um número: "))) 
    if 25>=x>=0:
        lista1.append(x)
    elif 50>=x>=26:
        lista2.append(x)
    elif 75>=x>=51:
        lista3.append(x)
    elif 100>=x>=76:
        lista4.append(x)
    if x < 0:
        break
print('Os números entre 0-25 são {}, entre 26-50 são {}, entre 51-75 são {} e entre 76-100 são {}.'.format(lista1, lista2, lista3, lista4))
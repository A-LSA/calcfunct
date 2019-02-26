def makecalc(a, b):
    x_values = (-1, 0, 1)
    for x in x_values:
        f_y_ = (a*x) + b
        print(f'{f_y_}, ', end='')
a = int(input('Digite o valor de A:'))
b = int(input('Digite o valor de B: '))
print('Os resultados são: ')
makecalc(a, b)


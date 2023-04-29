def leiaDinheiro(texto):
    control = False
    while not control:
        prec = str(input(texto)).replace(',', '.').strip()
        if prec.isalpha() or prec == '':
            print(f'\033[0;31mERRO: \"{prec}\" é um preço inválido!\033[m')
        else:
            return float(prec)

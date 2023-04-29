def moeda(preco=0, md='R$'):
    form = f'{md} {preco:>.2f}'.replace('.', ',')
    return form


def metade(preco=0, forma=False):
    met = preco / 2
    if forma == True:
        return moeda(met)
    else:
        return met



def dobro(preco=0, forma=False):
    dob = preco * 2
    if forma == True:
        return moeda(dob)
    else:
        return dob

def aumentar(preco=0, taxa=0, forma=False):
    aum = preco + (preco * (taxa/100))
    if forma == True:
        return moeda(aum)
    else:
        return aum


def diminuir(preco=0, taxa=0, forma=False):
    dim = preco - (preco * (taxa / 100))
    if forma == True:
        return moeda(dim)
    else:
        return dim


def resumo(preco, taxa_a=10, taxa_d=5):
    print('-' * 30)
    print(f'TABELA RESUMO'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'{taxa_a}% de aumento: \t{aumentar(preco, taxa_a, True)}')
    print(f'{taxa_d}% de redução: \t{diminuir(preco, taxa_d, True)}')
    print('-' * 30)

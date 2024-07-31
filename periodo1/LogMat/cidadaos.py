cidadaos = {'Bruno': 50,
    'Manfred': 40,
    'Klaus': 15}

idadeEleitoral = 16

for nome, idade in cidadaos.items():
    if idade >= idadeEleitoral:
        print(f'{nome} é eleitor')
    else:
        print(f'{nome} não é eleitor')
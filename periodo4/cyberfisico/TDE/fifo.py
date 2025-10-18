

lista_8quadros = []

lista_paginas1 = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7] # qual quadro na memória possuirá a página 7?
lista_paginas2 = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11] # qual quadro na memória possuirá a página 11?
lista_paginas3 = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11] # qual quadro na memória possuirá a página 11?

def mapeamento_memoria(lista_paginas):

    for pagina in lista_paginas:
        if pagina in lista_8quadros:
            print("pagina", pagina, "ja adicionada")
        else:
            print("page_fault, adicionando ", pagina)
            if len(lista_8quadros) >= 8:
                del lista_8quadros[0]
            lista_8quadros.append(pagina)
        print(lista_8quadros)
    return lista_8quadros

def main():
    mapeamento_memoria(lista_paginas1)
    # mapeamento_memoria(lista_paginas2)
    # mapeamento_memoria(lista_paginas3)

main()
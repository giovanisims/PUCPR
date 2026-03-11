
func exercicio10() {



    let carro = Carro(marca: "Marca do carro",modelo: "Modelo do carro",ano: 2026)

    print(carro.marca)
    print(carro.modelo)
    print(carro.ano)
}

    struct Carro {
    let marca: String
    let modelo: String
    let ano: Int
    }
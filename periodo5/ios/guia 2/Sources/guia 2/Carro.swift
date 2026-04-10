
class Carro {

    var marca:String
    let modelo:String

    var ano:Int{
        willSet {print("Ano alterado")}
    }

    init(_ marca:String, _ modelo:String, _ ano:Int) {
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    }
}

class Funcionario {
    var nome:String
    var salarioHora:Int = 20

    init(_ n:String) {
        self.nome = n
    }

    var calcularSalario:Int {
        return 30 * salarioHora
    }
}

class Pessoa: CustomStringConvertible {
    var nome:String
    var idade:Int

    init(_ n:String, _ i:Int) {
        self.nome = n;
        self.idade = i;
    }

    deinit {
        print("\(nome) foi removida do sistemas aos \(idade) anos")
    }

    var description: String {
        return "A \(nome) tem \(idade) anos"
    }
}

func exercicio2() {

    print("Escreva um número: ")
    if let input = readLine(), let numero = Int(input) {

        if numero % 2 == 0 {
            print("par")
        } else if numero % 2 != 0 {
            print("impar")
        } else {
            print("vc fez algm coisa errada")
        }
    }
}

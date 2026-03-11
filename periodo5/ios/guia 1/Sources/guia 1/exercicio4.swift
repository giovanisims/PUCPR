
func exercicio4() {
    var int1 = 0
    var int2 = 0

    print("Type the first number: ")
    if let input = readLine() {int1 = Int(input) ?? 0}
    print("Type the second number: ")
    if let input = readLine() {int2 = Int(input) ?? 0}

    print(soma(int1: int1, int2: int2))
}

func soma(int1: Int, int2: Int) -> Int {
    return int1 + int2
}


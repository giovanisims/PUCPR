
func exercicio8() {

    let letter = readLine()?.uppercased() 

    switch letter {
        case "A":
            print("Nota 10")
        case "B":
            print("Nota 9")
        case "C":
            print("Nota 8")
        case "D":
            print("Nota 7")
        case "F":
            print("Nota 0")
        default:
            ("escola A,B,C,D ou F")
    }
}
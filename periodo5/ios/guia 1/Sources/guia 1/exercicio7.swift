
func exercicio7() {

    var name: String? = "Giovani"

    if let name {print("Name is \(name)")}
    else {print("Name not defined")}

    name = nil
    guard let unpackedName = name else{print("Name not defined"); return }
    print("Name is \(name)")
}
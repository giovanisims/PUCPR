def main():
    decimal = get_decimal()
    dec_to_hex(decimal)

def get_decimal():
    while True:
        try:
            decimal = int(input("Enter a decimal number: "))
            return decimal
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

def dec_to_hex(decimal):
    hex_dict = {i: str(i) if i < 10 else chr(55 + i) for i in range(16)}
    hex_num = []
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        hex_num.insert(0, hex_dict[remainder])
    print(''.join(hex_num))

main()
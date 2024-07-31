def main():
    mass = float(input("Enter the initial mass of the substance: "))
    decay(mass)

def decay(m):
    time = 0
    while m > 0.5:
        m = m/2 
        time += 50
    print(f"{time} segundos")

main()
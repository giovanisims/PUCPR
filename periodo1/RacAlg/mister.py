import math
def main():
    txt = input("DIgite o maximo possivel em 60 segundos: ")
    txt_len = (len(txt) * 60)/1000
    print(math.ceil(txt_len))
main()
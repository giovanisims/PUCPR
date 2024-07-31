var = 70
for cont in range(20, 100, 10):
    if cont == var:
        print("Saindo antes")
        break
    var = var - 10
print("Var = ", var)

# cont20 var70
# cont30 var60
# cont40 var50
# cont50 var40
# cont60 var30
# cont70 var20
# cont80 var10
# cont90 var0
# cont100 var-10


var = 8
for cont_ext in range(4):
    for cont_int in range(4):
        if cont_ext == cont_int:
            print("Var = ", var)
print(cont_ext)

# Var =  8
# Var =  8
# Var =  8
# Var =  8
# 3



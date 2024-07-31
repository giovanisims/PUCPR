import math

oyear = int(input('Digite o seu ano de nascimento: '))
# initialize with an invalid value to make sure the condition is not satisfied

omonth = 0
while omonth not in range(1,13):
    omonth = int(input('Digite o mês do seu nascimento: '))
# initialize with an invalid value to make sure the condition is not satisfied
    
oday = 0
while oday not in range(1,32):
    oday = int(input('Digite o dia do seu nascimento: '))
nyear = int(input('Digite o ano atual: '))

nmonth = 0
while nmonth not in range(1,13):
    nmonth = int(input('Digite o mês atual: '))

nday = 0
while nday not in range(1,32):
    nday = int(input('Digite o dia atual: '))

age_day = abs(((oyear*12*31)+(omonth*31)+(oday))-((nyear*12*31)+(nmonth*31)+(nday)))

if age_day > 6696: print("Você pode dirigir! ")
else: days18 = abs(6696 - age_day)
    
if days18 < 31: 
    print(f"Você podrá dirigir em {days18} dias")
elif days18 >= 31:
    days18_2 = days18 % 31
    months18 = math.trunc(days18/31)
    if months18 <12:
        print(f"Você podrá dirigir em {days18_2} dias e {months18} meses")
    else:
        months18_2 = (months18 % 31)
        years18 = math.trunc(months18/12)
        print(f"Você podrá dirigir em {days18_2} dias, {months18_2} meses e {years18} anos")
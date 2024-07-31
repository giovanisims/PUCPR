# Enter the first time
firstHour = input("Qual é o primeiro horário (Ex: 07h23) ")
#Enter the second time
secondHour = input("Qual é o segundo horário (Ex: 07h23) ")

#Split the hours and minutes
hour1, minute1 = map(int,firstHour.split("h"))

hour2, minute2 = map(int,secondHour.split("h"))

# Multiply the hours
hour1convert = hour1 * 60
hour2convert = hour2 * 60
# add everything together
hour1minute = hour1convert + minute1
hour2minute = hour2convert + minute2

hourdiff = abs(hour2minute - hour1minute)

print("Passaram", hourdiff , "minutos" )
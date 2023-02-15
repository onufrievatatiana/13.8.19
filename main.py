tikets = int(input("Введите количество билетов "))
age = [int(input("Введите возраст участника ")) for i in range(tikets)]
prise = 0
for i in (age):
    if i < 18:
       prise += 0

    elif 18 <= i < 25:
       prise += 990

    else:
       prise += 1390
if tikets > 3:
    prise -= 0.1*prise

print("Общая стоимость билетов", prise, "руб.")






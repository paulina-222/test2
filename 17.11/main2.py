# #5
# x = int(input("podaj liczbe: "))
# x = x / 2 +4

# assert == 14


# #2.1
# a = input('Wprowadz imię:')
# b = input('Wprowadz nazwisko:')
# print(f"Cześć {a} {b}")

# #2.2
# x = input("nazwa pliku: ")
# print(x.split('.'))
# print(x.split('.')[1])



#2.3
# a = input('dzień:')
# b = input('miesiac:')
# c = input('rok:')

# print(a)
# print(b)
# print(c)

# print(f"{a}/{b}/{c}")


#2.4
# x = int(input('podaj liczbe:'))
# y = int(input('podaj liczbe:'))
# z = x + y

# print(f"Suma {x} oraz {y} to {z}")


# #2.5

# a = int(input('podaj liczbe:'))
# b = int(input('podaj liczbe:'))
# c = float(input('podaj liczbe:'))
# d = float(input('podaj liczbe:'))

# x = a + c
# print(x)
# print(type(x))
# y = d - b
# print(y)
# print(type(y))

# z = x + y
# print(z)



#2.6

# x = int(input('podaj liczbe:'))
# y = int(input('podaj stopien pierwiastka:'))


# print(f"Pierwiatek {y} stopnia z {x} to {x**(1/y)}")



#2.7
# słowo1 = str(input('podaj napis:'))
# słowo2 = str(input('podaj napis:'))

# print(f'{słowo1} {słowo2}')
# print(słowo1, słowo2, sep=", ")
# print(słowo1, end=" ")
# print(słowo2)


#2.8
# a = int(input('podaj bok a:'))
# b = int(input('podaj bok b:'))
# c = int(input('podaj bok c:'))

# p = 0.5 * (a+b+c)
# x = (p*(p-a)*(p-b)*(p-c)) ** (1/2)

# print(f"Pole trójkąta wynosi {x}")


#2.9
# kilometry = float(input('Podaj odleglość w km: '))
# mile = kilometry * 0.621371192

# print(f"{kilometry} kilometra to {mile:.2f} mili")


#2.9
c = float(input('Podaj temperature w C: '))
f = (c*9/5) + 32

print(f"{c} stopni Celcjusza to {f:.2f} Fahrenheita")
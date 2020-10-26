
# zad 1
napis = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle \n" \
        "poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza \n" \
        "do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle \n" \
        " elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach \n" \
        " 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem \n" \
        "Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym \n" \
        " do realizacji druków na komputerach osobistych, jak Aldus PageMaker \n"

print(napis)

# zad2
imie = "Kamil"
nazwisko = "Chomej"
litera_imie = imie[1]
litera_naziwsko = nazwisko[2]

print("W tekście jest ", napis.count(litera_imie), "liter oraz", napis.count(litera_naziwsko), "liter \n")

# zad3 - w pliku zad3

# zad4

zmienna_typu_string = "blablabla"

print(dir(zmienna_typu_string))
help(zmienna_typu_string.capitalize())

# zad5

imienaziwsko = "Kamil Chomej"[::-1].title()

print(imienaziwsko)

# zad6

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nowalista = lista[5:10]
lista = lista[0:5]

print(nowalista)
print(lista)

# zad7

lista.extend(nowalista)
lista.insert(0, 0)

kopialista = lista

print(sorted(kopialista, reverse=True))

# zad 8

krotka = ((1, "Jan Kowalski"), (2, "Kamil Chomej"), (3, "Robert Wiśniewski"), (4,  "Marcin Krawczyk"))

# zad 9
dict(krotka)

print(krotka)

# zad 10

listatel = [999999999, 123456789, 667304826, 232323232, 999999999, 670825666, 667304826]

print(list(set(listatel)))

# zad 11

liczby = range(1, 10)

for liczba in liczby:

    print(liczba)

# zad 12

liczby1 = reversed(range(20, 100))

for liczba in liczby1:

    if liczba % 5 == 0:
        print(liczba)

# zad 13

listaslownikow = [
    {
        'napis1': 1,
        'napis2': 2
    },
    {
        'napis3': 3,
        'napis4': 4
    },
    {
        'napis5': 5,
        'napis6': 6
    }
]

for x in listaslownikow:
    print(x)

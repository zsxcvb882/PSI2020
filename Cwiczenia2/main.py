from file_manager import FileManager

# zad1

def fun(a_list, b_list):
    c_list = a_list[::2] + b_list[1::2]
    return c_list


print(*fun([1, 2, 3, 4], [5, 6, 7, 8]), sep=", ")


# zad2


def fun2(data_text):
    dc = {
        "length": len(data_text),
        "letters": [char for char in data_text],
        "big_letters": data_text.upper(),
        "small_letters": data_text.lower()
    }
    return dc


print(fun2("doggy"))


# zad3


def fun3(text, letter):
    newtext = text.replace(letter, "")
    return newtext


print(fun3("hello", "l"))


# zad4


def fun4(value, temperature_type):
    if temperature_type == "cel":
        print("Fahrenheit: ", (value * 1.8) + 32)
        print("Rankine: ", (value + 273.15) * 1.8)
    elif temperature_type == "fahr":
        print("Celcjusz: ", (value - 32) / 1.8)
        print("Rankine: ", value + 457.67)
    elif temperature_type == "ren":
        print("Celcjusz: ", (value - 491.67) / 1.8)
        print("Fahrenheit: ", value - 457.67)
    else:
        print("Jako drugi parameter wpisz cel, fahr lub ren")


fun4(100, "fahr")


# zad5


class Calculator:

    @staticmethod
    def add(value1, value2):
        return value1 + value2

    @staticmethod
    def subtract(value1, value2):
        return value1 - value2

    @staticmethod
    def multiply(value1, value2):
        return value1 * value2

    @staticmethod
    def divide(value1, value2):
        return value1 / value2


print(Calculator.add(2, 3))


# zad6

class ScienceCalculator(Calculator):

    @staticmethod
    def exponentiation(value1, value2):
        return value1 ** value2


print(ScienceCalculator.exponentiation(3, 2))


# zad7


def fun7(text):
    return print(text[::-1])


fun7("koteł")

# zad8

# zad9

var1 = FileManager('testplik.txt')

var1.update_file('KolejneDodane')
var1.read_file()

# zad10


# -*- coding: utf-8 _*_


def foreign_exchange_calculator(ammount):
    cor_to_dol_rate = 33.80
    return cor_to_dol_rate * ammount


def run():
    print("C A L C U L A D O R A  D E  D I V I S A S\n")
    print("Convertir de USD a Cordobas\n")
    ammount = float(input("Cuantos dolares quieres convertir:\n"))

    result = foreign_exchange_calculator(ammount)
    print("La cantidad de ${} USD equivalen a ${} COR".format(ammount, result))


if __name__ == "__main__":
    run()

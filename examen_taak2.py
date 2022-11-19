#! python3

def voorwaartse_reeks(*args: str) -> str:
    return "".join(args).lower()


def achterwaartse_reeks(*args: str) -> str:
    return "".join(args).lower()[::-1]


def gemeenschappelijke_reeks(*args: str) -> str:
    voorwaarts = voorwaartse_reeks(*args)
    achterwaarts = achterwaartse_reeks(*args)
    for i in range(len(voorwaarts)):
        # print(voorwaarts[i:])
        # print(achterwaarts[:-i])
        if voorwaarts[i:] == achterwaarts[:-i]:
            return voorwaarts[i:] 
    return "" 


def ontbrekend_woord(*args: str) -> str:
    achterwaarts = achterwaartse_reeks(*args)
    gemeen = gemeenschappelijke_reeks(*args)
    return achterwaarts.lstrip(gemeen).capitalize()


def main():
    print(voorwaartse_reeks("Knalpot", "Tegengas", "Allebei", "Wegrenner", "Gewiebel", "Lasagne", "Getto"))
    print(achterwaartse_reeks("Knalpot", "Tegengas", "Allebei", "Wegrenner", "Gewiebel", "Lasagne", "Getto"))
    print(gemeenschappelijke_reeks("Knalpot", "Tegengas", "Allebei", "Wegrenner", "Gewiebel", "Lasagne", "Getto"))
    print(ontbrekend_woord("Knalpot", "Tegengas", "Allebei", "Wegrenner", "Gewiebel", "Lasagne", "Getto"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


import math


label = {# {{{
    "estado_civil" : 0,
    "instrucao"    : 1,
    "nfilho"       : 2,
    "salario"      : 3,
    "idade"        : 4,
    "meses"        : 5,
    "regiao"       : 6,
}# }}}


employees = [# {{{
    ("solteiro", "Fundamental", math.nan, 4.00, 26, 3, "interior"),
    ("casado", "Fundamental", 1, 4.56, 32, 10, "capital"),
    ("casado", "Fundamental", 2, 5.25, 36, 5, "capital"),
    ("solteiro", "Médio", math.nan, 5.73, 20, 10, "outro"),
    ("solteiro", "Fundamental", math.nan, 6.26, 40, 7, "outro"),
    ("casado", "Fundamental", 0, 6.66, 28, 0, "interior"),
    ("solteiro", "Fundamental", math.nan, 6.86, 41, 0, "interior"),
    ("solteiro", "Fundamental", math.nan, 7.39, 43, 4, "capital"),
    ("casado", "Médio", 1, 7.59, 34, 10, "capital"),
    ("solteiro", "Médio", math.nan, 7.44, 23, 6, "outro"),
    ("casado", "Médio", 2, 8.12, 33, 6, "interior"),
    ("solteiro", "Fundamental", math.nan, 8.46, 27, 11, "capital"),
    ("solteiro", "Médio", math.nan, 8.74, 37, 5, "outro"),
    ("casado", "Fundamental", 3, 8.95, 44, 2, "outro"),
    ("casado", "Médio", 0, 9.13, 30, 5, "interior"),
    ("solteiro", "Médio", math.nan, 9.35, 38, 8, "outro"),
    ("casado", "Médio", 1, 9.77, 31, 7, "capital"),
    ("casado", "Fundamental", 2, 9.80, 39, 7, "outro"),
    ("solteiro", "Superior", math.nan, 10.53, 25, 8, "interior"),
    ("solteiro", "Médio", math.nan, 10.76, 37, 4, "interior"),
    ("casado", "Médio", 1, 11.06, 30, 9, "outro"),
    ("solteiro", "Médio", math.nan, 11.59, 34, 2, "capital"),
    ("solteiro", "Fundamental", math.nan, 12.00, 41, 0, "outro"),
    ("casado", "Superior", 0, 12.79, 26, 1, "outro"),
    ("casado", "Médio", 2, 13.23, 32, 5, "interior"),
    ("casado", "Médio", 2, 13.60, 35, 0, "outro"),
    ("solteiro", "Fundamental", math.nan, 13.85, 46, 7, "outro"),
    ("casado", "Médio", 0, 14.69, 29, 8, "interior"),
    ("casado", "Médio", 5, 14.71, 40, 6, "interior"),
    ("casado", "Médio", 2, 15.99, 35, 10, "capital"),
    ("solteiro", "Superior", math.nan, 16.22, 31, 5, "outro"),
    ("casado", "Médio", 1, 16.61, 36, 4, "interior"),
    ("casado", "Superior", 3, 17.26, 43, 7, "capital"),
    ("solteiro", "Superior", math.nan, 18.75, 33, 7, "capital"),
    ("casado", "Médio", 2, 19.40, 48, 11, "capital"),
    ("casado", "Superior", 3, 23.30, 42, 2, "interior"),
]# }}}


def main():
    for eee in employees:
        if eee[label['regiao']] == 'interior' and eee[label['estado_civil']] == 'casado':
            print(eee)


if __name__ == "__main__":
    main()

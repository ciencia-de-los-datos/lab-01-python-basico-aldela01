"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

csv_file = 'data.csv'

with open(csv_file, 'r') as f:
        reader = csv.reader(f,delimiter='\t')
        data = list(reader)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    

    second_column = [row[1] for row in data]

    second_column = [int(i) for i in second_column]
    s=sum(second_column)    

    return s


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    first_column = [row[0] for row in data]
    first_column = sorted(first_column)

    #Convert first_column to a dictionary with a 1 as the value for each key

    first_column_tuples = [(i,1) for i in first_column]

    first_column_tuples_dict = {}

    for key, value in first_column_tuples:
        if key not in first_column_tuples_dict:
            first_column_tuples_dict[key] = 0
        first_column_tuples_dict[key]+=value

    #Convert first_column_tuples_dict to a list of tuples
        
    first_column_tuples = list(first_column_tuples_dict.items())
    return first_column_tuples


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    first_second_column = [(row[0],int(row[1])) for row in data]

    first_second_column = sorted(first_second_column)

    first_second_column_dict = {}

    for key, value in first_second_column:
        if key not in first_second_column_dict:
            first_second_column_dict[key] = 0
    first_second_column_dict[key]+=value

    first_second_column = list(first_second_column_dict.items())
    return first_second_column


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    third_column = sorted([(row[2].split('-')[1],1) for row in data])
    third_column_dict = {}

    for key, value in third_column:
        if key not in third_column_dict:
            third_column_dict[key] = 0
        third_column_dict[key]+=value

    third_column = list(third_column_dict.items())
    return third_column


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    first_second_column = [(row[0],int(row[1])) for row in data]

    first_second_column = sorted(first_second_column)

    first_second_column_dict = {}

    for key, value in first_second_column:
        if key not in first_second_column_dict:
            first_second_column_dict[key] = []
        first_second_column_dict[key].append(value)
    first_second_column_dict={key:(max(value),min(value)) for key, value in first_second_column_dict.items()}

    first_second_column = list(first_second_column_dict.items())
    first_second_column = [(i[0],i[1][0],i[1][1]) for i in first_second_column]
    return first_second_column


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    fifth_column = [row[4].split(',') for row in data]
    fifth_column = sorted([i for sublist in fifth_column for i in sublist])
    fifth_column = [i.split(':') for i in fifth_column]

    fifth_column_dict = {}

    for key, value in fifth_column:
        if key not in fifth_column_dict:
            fifth_column_dict[key] = []
        fifth_column_dict[key].append(int(value))
    fifth_column_dict={key:(min(value),max(value)) for key, value in fifth_column_dict.items()}

    fifth_column = list(fifth_column_dict.items())
    fifth_column = [(i[0],i[1][0],i[1][1]) for i in fifth_column]

    return fifth_column


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    second_first_column = [(int(row[1]),row[0]) for row in data]

    second_first_column_dict = {}

    for key, value in second_first_column:
        if key not in second_first_column_dict:
            second_first_column_dict[key] = []
        second_first_column_dict[key].append(value)

    second_first_column = sorted(list(second_first_column_dict.items()))
    return second_first_column


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    second_first_column = pregunta_07()
    second_first_column_set=[(row[0],sorted(list(set(row[1])))) for row in second_first_column]

    return second_first_column_set


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    fifth_column = [row[4].split(',') for row in data]
    fifth_column = sorted([i for sublist in fifth_column for i in sublist])
    fifth_column = [i.split(':') for i in fifth_column]

    fifth_column_tuples = [(i[0],1) for i in fifth_column]

    fifth_column_tuples_dict = {}

    for key, value in fifth_column_tuples:
        if key not in fifth_column_tuples_dict:
            fifth_column_tuples_dict[key] = 0
        fifth_column_tuples_dict[key]+=value

    fifth_column_tuples = list(fifth_column_tuples_dict.items())
    return fifth_column_tuples


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    first_fourth_fifth_column = [(row[0],len(row[3].split(',')),len(row[4].split(','))) for row in data]
    return first_fourth_fifth_column


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    
    """

    fourth_second_column=[(row[3].split(','),int(row[1])) for row in data]

    fourth_second_column_tuples=sorted([(row[0][i],row[1]) for row in fourth_second_column for i in range(len(row[0]))])
    fourth_second_column_tuples_dict = {}

    for key, value in fourth_second_column_tuples:
        if key not in fourth_second_column_tuples_dict:
            fourth_second_column_tuples_dict[key] = 0
        fourth_second_column_tuples_dict[key]+=value
    return fourth_second_column_tuples_dict


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    first_column = [row[0] for row in data]
    fifth_column = [row[4].split(',') for row in data]
    fifth_column = [[i.split(':') for i in row] for row in fifth_column]
    fifth_column = [sum([int(i[1]) for i in row]) for row in fifth_column]

    first_fifth_column = sorted(list(zip(first_column,fifth_column)))
    first_fifth_column_dict={}
    for key, value in first_fifth_column:
        if key not in first_fifth_column_dict:
            first_fifth_column_dict[key] = 0
        first_fifth_column_dict[key]+=value
    return first_fifth_column_dict

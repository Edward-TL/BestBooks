import csv, os
import re


def Load_And_Max(file, ColumnName):
    with open(books, mode="r", encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        max_rate = 0
        ArrayColumn = []
        

        for row in csv_reader:
            """Sinceramente, no encontré la forma de hacer que identifique cuando no es un numero."""
            """Intente RegEx, isalpha y cachar el error en caso de que no pudeira convertir el float."""
            """Asi que sí me puedes ayudar con esto, te lo agradecería infinitamente por que sí me tocó corregir esto a mano en mis anteriores trabajos"""
            if len(row[ColumnName]) <= 4: 
                ArrayColumn.append(float(row[ColumnName]))
                

                if float(row[ColumnName]) > max_rate:
                    max_rate = float(row[ColumnName])
            else:
                ArrayColumn.append("DOSN'T COUNT!")

    csv_file.close()

    return ArrayColumn, max_rate

def SearchArrayDir(Array, SearchValue):
    ArrayOfEquals = []
    dir_counter = 0
    SearchValue = str(SearchValue)
    ErrorArray = []

    for element in range(len(Array)):
        if Array[dir_counter] == "DOSN'T COUNT!":
            print(f'si entró en {dir_counter} a {Array[dir_counter]}')
            ErrorArray.append(dir_counter)
        else:
            if str(Array[dir_counter]) == SearchValue:
                    print(f'{dir_counter} Entro {Array[dir_counter]} al == {SearchValue} ')
                    ArrayOfEquals.append(dir_counter)
        dir_counter += 1
    
    print(ErrorArray)
    return ArrayOfEquals



if __name__=='__main__':
    bookID = []
    title = []
    rate = []
    # THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    books = os.path.join(cwd,'test01.csv')

    rates, max_rate = Load_And_Max(books,"average_rating")

    print(rate)
    print(max_rate)
    MaxDirs = SearchArrayDir(rates, max_rate)
    print(MaxDirs)
    # ExtractTable(books, rate, max_rate, "title", "average_rating")


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
            ErrorArray.append(dir_counter)
        else:
            if str(Array[dir_counter]) == SearchValue:
                    ArrayOfEquals.append(dir_counter)
        dir_counter += 1
    
    # print(ErrorArray)
    return ArrayOfEquals

def ChunkTable(file, DirArray, RateHeader, TitleHeader, ConsiderHeader):
    with open(books, mode="r", encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_counter = 0
        dir_counter = 0
        print(' Rate  |  Title')
        print('------ | -------')
        
        if ConsiderHeader == False:
            for element in range(len(DirArray)):
                DirArray[element] += 1

        for row in csv_reader:
            if line_counter == DirArray[dir_counter]-1:
                print(f'   {row[RateHeader]}      {row[TitleHeader]}')
                dir_counter += 1
            
            if dir_counter == (len(DirArray)):
                print('------ | -------')
                break

            line_counter += 1

    csv_file.close()

    if ConsiderHeader == False:
            for element in range(len(DirArray)):
                DirArray[element] -= 1

def ExtractFromTable(file, DirArray, RateHeader, TitleHeader, ConsiderHeader):
    with open(books, mode="r", encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_counter = 0
        dir_counter = 0
        RateHeaderArray = []
        TitleHeaderArray = []

        if ConsiderHeader == False:
            for element in range(len(DirArray)):
                DirArray[element] += 1

        for row in csv_reader:
            if line_counter == DirArray[dir_counter]-1:
                RateHeaderArray.append(row[RateHeader])
                TitleHeaderArray.append(row[TitleHeader])
                dir_counter += 1
            
            if dir_counter == (len(DirArray)):
                break

            line_counter += 1

    csv_file.close()

    return RateHeaderArray, TitleHeaderArray

if __name__=='__main__':
    bookID = []
    title = []
    rate = []
    cwd = os.getcwd()
    books = os.path.join(cwd,'test01.csv')

    rates, max_rate = Load_And_Max(books,"average_rating")

    MaxDirs = SearchArrayDir(rates, max_rate)
    """Esto es para el caso en que solo quiero imprimir la tabla, sin extraer la información. O sea, solo ver"""
    print('\nEjemplo 1:')
    ChunkTable(books, MaxDirs, "average_rating", "title", False)

    """Esto es para el caso en que quiero extraer los datos de la tabla para interactuar con ellos"""
    BestRateArray, BestTitlesArray = ExtractFromTable(books, MaxDirs, "average_rating", "title", False)
    print('\nEjemplo 2:')
    print(' Rate  |  Title')
    print('------ | -------')
    
    for i in range(len(BestRateArray)):
        print(f'   {BestRateArray[i]}      {BestTitlesArray[i]}')
    # ExtractTable(books, rate, max_rate, , "average_rating")


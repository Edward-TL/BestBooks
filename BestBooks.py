import csv, os


def Load_And_Max(file, ColumnName):
    with open(books, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        max_rate = 0
        ArrayColumn = []

        for row in csv_reader:
            if isinstance(float(row[ColumnName]), float) == True:
                ArrayColumn.append(float(row[ColumnName]))

                if float(row[ColumnName]) > max_rate:
                    max_rate = float(row[ColumnName])

    csv_file.close()

    return ArrayColumn, max_rate

def BestRated(file, RateArray, BestRate, TitleHeader, RateHeader):
    BestRatedArray = RateArray
    TitleArray = []

    with open(books, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_counter = 0
        for row in csv_reader:
            if line_counter == 0:
                line_counter += 1
            TitleArray.append(row[TitleHeader])


    csv_file.close()
    print(' Rate  ', '  Title')
    print('------ ', ' -------')
    for i in range(len(BestRatedArray)):
        print(f' {BestRatedArray[i]}     {TitleArray[i]}')

if __name__=='__main__':
    bookID = []
    title = []
    rate = []
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    books = os.path.join(THIS_FOLDER, 'files/test01.csv')

    rate, max_rate = Load_And_Max(books,"average_rating")

    print(rate)
    print(max_rate)
    BestRated(books, rate, max_rate, "title", "average_rating")

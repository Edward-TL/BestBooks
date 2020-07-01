import csv, os
from datetime import datetime

def LoadAndMax(file, ColumnToFind):
    with open(books, mode="r", encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        header = next(csv_reader)
        ColumnArray = []
        Max_value = 0

        for row in csv_reader:
            try:
                last_row = row[12]
                if last_row == '':
                    last_row = row[13]

                if ColumnToFind == 'average_rating': Column_data = float(row[4])
                elif ColumnToFind == 'num_pages': Column_data = int(row[8])
                elif ColumnToFind == 'ratings_count': Column_data = int(row[9])
                elif ColumnToFind == 'text_reviews_count': Column_data = int(row[10])
                else:
                    ColumnArray = 'Data not Found. Check input'
                    Max_value = 0
                    return ColumnArray, Max_value
            except IndexError:
                if ColumnToFind == 'average_rating': Column_data = float(row[3])
                elif ColumnToFind == 'num_pages': Column_data =  int(row[7])
                elif ColumnToFind == 'ratings_count': Column_data = int(row[8])
                elif ColumnToFind == 'text_reviews_count': Column_data = int(row[9])
                else:
                    ColumnArray = 'Data not Found. Check input'
                    Max_value = 0
                    return ColumnArray, Max_value

            ColumnArray.append(Column_data)
            if Column_data > Max_value:
                Max_value = Column_data

    csv_file.close()

    return ColumnArray, Max_value

def MergeSort(Array):
    if len(Array) > 1:
        middle = len(Array) // 2
        Left = Array[:middle]
        Right = Array[middle:]

        MergeSort(Left)
        MergeSort(Right)
        
        """SubArrays Iterators"""
        i = 0
        j = 0
        """MainArray Iterator"""
        k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                Array[k] = Left[i]
                i += 1
            else:
                Array[k] = Right[j]
                j += 1
            
            k += 1

        while i < len(Left):
            Array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            Array[k] = Right[j]
            j += 1
            k += 1

    return Array

def TopXOrdered(Array, TopSize):
    """Considerations.
    1) Array is ORDERED from minor to major.
    2) You can insert Arrays with duplicated values.
    3) You won't insert Sets."""

    TopX = []
    position = len(Array) - 1
    
    value = Array[position]
    TopX.append(value)

    position -= 1
    max_value = value
    value = Array[position]

    TopValues = 1 

    while TopValues < TopSize and position >= 0 :
        if value != max_value:
            TopX.append(Array[position])
            max_value = value
            TopValues += 1
        position -= 1
        value = Array[position]

        

    return TopX

def ObtainArrays(file):
    with open(books, mode="r", encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = []
        
        for row in csv_reader:
            try:
                last_row = row[12]
                if last_row == '':
                    last_row = row[13]

                title = row[1]
                authors = row[2] + ',' + row[3]
                average_rating = float(row[4])
                isbn = row[5]
                isbn13 = row[6]
                lenguage = row[7]
                num_pages = int(row[8])
                ratings_count = int(row[9])
                text_reviews = int(row[10])
                publication_date = datetime.strptime(row[11], '%m/%d/%Y')
                publisher = row[12]

            except IndexError:
                title = row[1]
                authors = row[2]
                average_rating = float(row[3])
                isbn = row[4]
                isbn13 = row[5]
                lenguage = row[6]
                num_pages =  int(row[7])
                ratings_count = int(row[8])
                text_reviews = int(row[9])
                publication_date = datetime.strptime(row[10], '%m/%d/%Y')
                publisher = row[11]
                
            data.append([title, authors, average_rating, isbn, isbn13, lenguage,
                        num_pages, ratings_count, text_reviews, publication_date, publisher])

    csv_file.close()

    return data

if __name__=='__main__':
    cwd = os.getcwd()
    books = os.path.join(cwd,'tests/test05.csv')
    
    rating, max_rating = LoadAndMax(books, 'average_rating')

    rating = MergeSort(rating)
    top5_rating = TopXOrdered(rating, 5)
    print(top5_rating)

    
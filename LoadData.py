import csv, os
from datetime import datetime


def LoadBooks(file):
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
                num_pages = int(row[7])
                ratings_count = int(row[8])
                text_reviews = int(row[9])
                publication_date = row[10]
                publication_date = datetime.strptime(publication_date, '%m/%d/%Y')
                publisher = row[11]

            data.append([title, authors, average_rating, isbn, isbn13, lenguage,
                        num_pages, ratings_count, text_reviews, publication_date, publisher])
            
            

            # if row_Data == numberID[0]: 
            #     ArrayColumn.append(float(row[ColumnName]))
                
            #     if float(row[ColumnName]) > max_rate:
            #         max_rate = float(row[ColumnName])
            # else:
            #     ArrayColumn.append("DOSN'T COUNT!")

            # counter += 1


    csv_file.close()

    return header, data



if __name__=='__main__':
    bookID = []
    title = []
    rate = []
    cwd = os.getcwd()
    books = os.path.join(cwd,'test05.csv')

    header, data = LoadBooks(books)
    print(f'HEADER: {header}')
    for row in range(len(data)):
        print(f'Datos en fila {row}: {data[row]}')
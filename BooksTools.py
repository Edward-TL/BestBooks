import csv, os
from datetime import datetime

def load_and_max(file, column_to_find):
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

                if column_to_find == 'average_rating': Column_data = float(row[4])
                elif column_to_find == 'num_pages': Column_data = int(row[8])
                elif column_to_find == 'ratings_count': Column_data = int(row[9])
                elif column_to_find == 'text_reviews_count': Column_data = int(row[10])
                else:
                    ColumnArray = 'Data not Found. Check input'
                    Max_value = 0
                    return ColumnArray, Max_value
            except IndexError:
                if column_to_find == 'average_rating': Column_data = float(row[3])
                elif column_to_find == 'num_pages': Column_data =  int(row[7])
                elif column_to_find == 'ratings_count': Column_data = int(row[8])
                elif column_to_find == 'text_reviews_count': Column_data = int(row[9])
                else:
                    ColumnArray = 'Data not Found. Check input'
                    Max_value = 0
                    return ColumnArray, Max_value

            ColumnArray.append(Column_data)
            if Column_data > Max_value:
                Max_value = Column_data

    csv_file.close()

    return ColumnArray, Max_value

def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        Left = array[:middle]
        Right = array[middle:]

        merge_sort(Left)
        merge_sort(Right)
        
        """SubArrays Iterators"""
        i = 0
        j = 0
        """MainArray Iterator"""
        k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            
            k += 1

        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1

    return array

def topx_ordered(array, top_size):
    """Considerations.
    1) Array is ORDERED from minor to major.
    2) You can insert Arrays with duplicated values.
    3) You won't insert Sets."""

    TopX = []
    position = len(array) - 1
    
    value = array[position]
    TopX.append(value)

    position -= 1
    max_value = value
    value = array[position]

    TopValues = 1 

    while TopValues < top_size and position >= 0 :
        if value != max_value:
            TopX.append(array[position])
            max_value = value
            TopValues += 1
        position -= 1
        value = array[position]

        

    return TopX

def obtain_arrays(file):
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

def counted_array(elements_to_count, original_array):
    CountArray = []
    for value in range(len(elements_to_count)):
        CountArray.append(original_array.count(elements_to_count[value]))
    
    return CountArray

def sorted_and_reduce(array):
    ReducedSet = set(array)
    ReducedArray = []
    for element in ReducedSet:
        ReducedArray.append(element)
    ReducedArray = merge_sort(ReducedArray)

    return ReducedArray

def match_cases(array1, wanted_array1, array2, wanted_array2):
    """Notice de diference: the original data has to be of the samen lenght,
    BUT the match cases can differ. This means that I can have 3 match cases
    on one side and 50 in the other, and it won't make any trouble"""
    if len(array1)==len(array2):
        match_cases = []

        #Creating Support dictionaries
        wanted_cases_1 = {}
        for data in range(len(wanted_array1)):
            wanted_cases_1[wanted_array1[data]] = 1
        
        wanted_cases_2 = {}
        for data in range(len(wanted_array2)):
            wanted_cases_2[wanted_array2[data]] = 1
        
        for ub in range(len(array1)):
            val1 = array1[ub]
            val2 = array2[ub]
            if val1 in wanted_cases_1 and val2 in wanted_array2:
                print(f'Val 1: {val1}, Val 2: {val2}')
                match_cases.append(ub)
            
        
        return match_cases

    else: return 'Arrays must have the samen lenght'


if __name__=='__main__':
    cwd = os.getcwd()
    books = os.path.join(cwd,'books.csv')
    
    rating, max_rating = load_and_max(books, 'average_rating')
    reviews, max_reviews = load_and_max(books, 'text_reviews_count')
    
    or_rating = rating.copy()
    or_reviews = reviews.copy()

    ordered_rating = merge_sort(rating)
    ordered_reviews = merge_sort(reviews)

    top_rating = topx_ordered(ordered_rating, 32)
    top_reviews = topx_ordered(ordered_reviews, 952)
    # print(f'TOP5 Rating: {top5_rating} Reviews: {top_reviews}')
    # print(f'RATING: {or_rating[:15]}')

    match_cases = match_cases(or_rating, top_rating, or_reviews, top_reviews)
    print(match_cases)
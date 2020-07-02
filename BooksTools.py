import csv, os
from datetime import datetime

def load_and_max(file, column_to_find):
    with open(books, mode="r", encoding='utf-8', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        header = next(csv_reader)
        column_array = []
        max_value = 0

        for row in csv_reader:
            try:
                last_row = row[12]
                if last_row == '':
                    last_row = row[13]

                if column_to_find == 'average_rating': column_data = float(row[4])
                elif column_to_find == 'num_pages': column_data = int(row[8])
                elif column_to_find == 'ratings_count': column_data = int(row[9])
                elif column_to_find == 'text_reviews_count': column_data = int(row[10])
                else:
                    column_array = 'Data not Found. Check input'
                    max_value = 0
                    return column_array, max_value
            except IndexError:
                if column_to_find == 'average_rating': column_data = float(row[3])
                elif column_to_find == 'num_pages': column_data =  int(row[7])
                elif column_to_find == 'ratings_count': column_data = int(row[8])
                elif column_to_find == 'text_reviews_count': column_data = int(row[9])
                else:
                    column_array = 'Data not Found. Check input'
                    max_value = 0
                    return column_array, max_value

            column_array.append(column_data)
            if column_data > max_value:
                max_value = column_data

    csv_file.close()

    return column_array, max_value

def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)
        
        """SubArrays Iterators"""
        i = 0
        j = 0
        """MainArray Iterator"""
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

def binary_search(array, start, end, search_value):
    if start > end:
        return end
    
    middle = (start + end) // 2

    if array[middle] == search_value:
        return middle
    elif array[middle] < search_value:
        return binary_search(array, middle + 1, end, search_value)
    else:
        return binary_search(array, start, middle - 1, search_value)
    
def topx(array, top_size):
    """Considerations.
    1) Array is ORDERED from minor to major.
    2) You can insert Arrays with duplicated values.
    3) You won't insert Sets."""

    sorted_and_reduced_array = sorted_and_reduce(array.copy())
    position = len(sorted_and_reduced_array) - 1
    
    topx = []
    value = sorted_and_reduced_array[position]
    topx.append(value)

    position -= 1
    max_value = value
    value = sorted_and_reduced_array[position]

    top_values = 1 

    while top_values < top_size and position >= 0 :
        if value != max_value:
            topx.append(sorted_and_reduced_array[position])
            max_value = value
            top_values += 1
        position -= 1
        value = sorted_and_reduced_array[position]

        

    return topx

def top_condisioned(array, start_value):
    helper_array = sorted_and_reduce(array.copy())
    helpers_end = len(helper_array) - 1
    ubication =  binary_search(helper_array, 0, helpers_end, start_value)
    
    top_condisioned = []
    for i in range(ubication, helpers_end):
        top_condisioned.append(helper_array[i])

    return top_condisioned

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
    count_array = []
    for value in range(len(elements_to_count)):
        count_array.append(original_array.count(elements_to_count[value]))
    
    return count_array

def sorted_and_reduce(array):
    reduced_set = set(array)
    reduced_array = []
    for element in reduced_set:
        reduced_array.append(element)
    reduced_array = merge_sort(reduced_array)

    return reduced_array

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
                match_cases.append(ub)
            
        return match_cases

    else: return 'Arrays must have the samen lenght'

if __name__=='__main__':
    cwd = os.getcwd()
    books = os.path.join(cwd,'books.csv')
    
    rating, max_rating = load_and_max(books, 'average_rating')
    reviews, max_reviews = load_and_max(books, 'text_reviews_count')

    topc_rating = top_condisioned(rating, 4.5)
    topc_reviews = top_condisioned(reviews, 1000)

    top_rating = topx(rating, 32)
    top_reviews = topx(reviews, 952)
    # print(f'TOP5 Rating: {top5_rating} Reviews: {top_reviews}')
    # print(f'RATING: {or_rating[:15]}')

    match_cases = match_cases(rating, topc_rating, reviews, topc_reviews)
    print(match_cases)
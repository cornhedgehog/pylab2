from app.model.book import BookDAO, get_list

BOOK_PAGE_FIELD = 'total_page_number'
BOOK_DATE_FIELD = 'first_publication_date'

def get_books():
   return get_list()

def get_books_sorted(is_author_sort, is_title_sort, is_genre_sort, is_date_sort, is_page_sort, sort_oder):
    is_desc = sort_oder == 'desc' or False
    result = get_list()
    if is_author_sort:
        result = sorted(result, key=lambda obj: obj['author_full_name'], reverse=is_desc)
    if is_title_sort:
       result = sorted(result, key=lambda obj: obj['book_name'], reverse=is_desc)
    if is_genre_sort:
       result = sorted(result, key=lambda obj: obj['genre'], reverse=is_desc)
    if is_date_sort:
       result = sorted(result, key=lambda obj: obj['first_publication_date'], reverse=is_desc)
    if is_page_sort:
       result = sorted(result, key=lambda obj: obj['total_page_number'], reverse=is_desc)
    return result

def get_avg_date():
    result = get_list()
    total_sum = 0
    for r in result:
        total_sum += r[BOOK_DATE_FIELD]
    return total_sum / len(result)

def get_avg_page_number():
    result = get_list()
    total_sum = 0
    for r in result:
        total_sum += r[BOOK_PAGE_FIELD]
    return total_sum / len(result)

def get_min_date():
    result = get_list()
    if len(result) == 0:
        return 0
    min = result[0][BOOK_DATE_FIELD]
    for r in result:
        if min > r[BOOK_DATE_FIELD]:
            min = r[BOOK_DATE_FIELD]
    return min

def get_min_page_number():
    result = get_list()
    if len(result) == 0:
        return 0
    min = result[0][BOOK_PAGE_FIELD]
    for r in result:
        if min > r[BOOK_PAGE_FIELD]:
            min = r[BOOK_PAGE_FIELD]
    return min

def get_max_date():
    result = get_list()
    if len(result) == 0:
        return 0
    max = result[0][BOOK_DATE_FIELD]
    for r in result:
        if max < r[BOOK_DATE_FIELD]:
            max = r[BOOK_DATE_FIELD]
    return max

def get_max_page_number():
    result = get_list()
    if len(result) == 0:
        return 0
    max = result[0][BOOK_PAGE_FIELD]
    for r in result:
        if max < r[BOOK_PAGE_FIELD]:
            max = r[BOOK_PAGE_FIELD]
    return max
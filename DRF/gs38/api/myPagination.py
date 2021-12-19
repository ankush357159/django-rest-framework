from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'records'
    max_page_size = 7
    # page_query_param = 'page_number'
    # page_query_param - A string value indicating the name of the query parameter to use for the pagination control
from rest_framework.pagination import PageNumberPagination


class ProductsPagination(PageNumberPagination):
    """Пагинатор для получения продуктов постранично"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

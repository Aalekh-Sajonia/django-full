from rest_framework.pagination import LimitOffsetPagination, CursorPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 5

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
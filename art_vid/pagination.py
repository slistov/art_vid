from mmap import PAGESIZE
from rest_framework import pagination # PageNumberPagination


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return pagination.Response({
            'data': data,
            'meta': {
                'current_page': self.page.number,
                'last_page': self.page.paginator.num_pages,
                'per_page': self.page.paginator.per_page,
                'total': self.page.paginator.count
            },            
        })
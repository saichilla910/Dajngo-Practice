from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
class CustompaginationForProducts(PageNumberPagination):
    page_size_query_param='page_size'
    page_query_param='page_num'
    max_page_size=2
    def get_paginated_response(self, data):
        return  Response(
            {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'page_size': self.get_page_size(self.request),
                'results': data
            }
        )
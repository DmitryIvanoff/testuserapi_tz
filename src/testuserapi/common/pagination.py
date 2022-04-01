from collections import OrderedDict

from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class TestUserAPIPagination(PageNumberPagination):

    page_size_query_param = "per_page"

    def __init__(self):
        super().__init__()
        self.paginator = None
        self.page = None
        self.request = None

    def paginate_queryset(self, queryset, request, view=None):
        """
        Добавил сохранение paginator в свойствах LetovoPagination
        """

        page_size = self.get_page_size(request)
        if not page_size:
            return None

        self.paginator = self.django_paginator_class(queryset, page_size)
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = self.paginator.num_pages

        try:
            self.page = self.paginator.page(page_number)
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(
                page_number=page_number, message=str(exc)
            )
            raise NotFound(msg)

        if self.paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("current_page", self.page.number),
                    ("last_page", self.paginator.num_pages),
                    ("total", self.paginator.count),
                    ("per_page", self.paginator.per_page),
                    ("next_page_url", self.get_next_link()),
                    ("prev_page_url", self.get_previous_link()),
                    ("data", data),
                ]
            )
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "current_page": {
                    "type": "integer",
                    "example": 1,
                },
                "last_page": {
                    "type": "integer",
                    "example": 1,
                },
                "total": {
                    "type": "integer",
                    "example": 123,
                },
                "next_page_url": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?{page_query_param}=4".format(
                        page_query_param=self.page_query_param
                    ),
                },
                "prev_page_url": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?{page_query_param}=2".format(
                        page_query_param=self.page_query_param
                    ),
                },
                "data": schema,
            },
        }


class StandardPagination(PageNumberPagination):
    page_size_query_param = "page_size"

# import logging
# import uuid
# from typing import Dict  # noqa

# from .services import BookService

from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models.shops import Shop

# logger = logging.getLogger(__name__)


class ShopsAPI(ViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def list(self, request):
        queryset = Shop.objects.all()
        return Response(queryset)


# class BookAPI:

#     @staticmethod
#     def get(*, book_id: uuid.UUID) -> Dict:
#         logger.info('method "get" called')
#         return BookService.get_book(id=book_id)

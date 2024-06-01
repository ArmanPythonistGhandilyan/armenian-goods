# # - services.py - coordination and transactional logic.

# Services
# Everything in a domain comes together in Services.

# Services gather all the business value for this domain. What type of logic should live here? Here are a few examples:

# When creating a new instance of a model, we need to compute a field on it before saving.
# When querying some content, we need to collect it from a few different places and gather it together in a python object.
# When deleting an instance we need to send a signal to another domain so it can do it's own logic.
# Anything that is specific to the domain problem and not basic informational logic should live in Services. As most API projects expose single functional actions such as Create, Read, Update, and Delete, Services has been designed specifically to compliment stateless, single-action functions.

# A services.py file could look like:

# import logging
# import uuid
# from typing import Dict, Str  # noqa

# from .interfaces import AuthorInterface
# from .models import Book

# logger = logging.getLogger(__name__)


# # Plain example
# def get_book(*, id: uuid.UUID) -> Dict:
#     book = Book.objects.get(id=id)
#     author = AuthorInterface.get_author(id=book.author_id)
#     return {
#         'name': book.name,
#         'author_name': author.name,
#     }


# # Class example
# class PGMNodeService:

#     @staticmethod
#     def get_book(*, id: uuid.UUID) -> Dict:
#         book = Book.objects.get(id=id)
#         author = AuthorInterface.get_author(id=book.author_id)
#         return {
#             'name': book.name,
#             'author_name': author.name,
#         }

#     @staticmethod
#     def create_book(*, name: Str, author_id: uuid.UUID) -> Dict:
#         logger.info('Creating new book')
#         new_book = Book.objects.create(name=name, author_id=author_id)
#         author = AuthorInterface.get_author(id=new_book.author_id)
#         return {
#             'name': new_book.name,
#             'author_name': author.name,
#         }

#     @staticmethod
#     def update_book_name_and_author_name(
#         *,
#         name: Str,
#         author_name: Str,
#         author_id: uuid.UUID,
#         id: uuid.UUID,
#     ) -> Dict:
#         logger.info('Updating book name and author name')
#         book = Book.objects.get(id=id).update(name=name)
#         author = AuthorInterface.update_author_name(
#             name=author_name, id=author_id,
#         )
#         return {
#             'name': book.name,
#             'author_name': author.name,
#         }

# The primary components of Services should be functions.
# Services should own co-ordination and transactional logic.
# You can group functions under a class if it makes sense for organisation.
# If you are using a class, it must use the naming convention MyDomainService.
# Functions in services.py must use type annotations.
# Functions in services.py must use keyword arguments.
# You should be logging in services.py.
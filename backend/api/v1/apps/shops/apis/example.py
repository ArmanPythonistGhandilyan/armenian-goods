# APIs
# APIs defines the external API interface for your domain. Anyone using the APIs defined here is called a consumer. The API can be either an HTTP API using GraphQL or REST for consumers over the web, or a software API for internal consumers. APIs is defined in apis.py which is agnostic to the implementation you choose, you can even put more than one API in a domain. For example - you might want to wrap a GraphQL API and a REST API around your domain for different consumers.

# An apis.py file that defines a simple software API can look like:

# import logging
# import uuid
# from typing import Dict  # noqa

# from .services import BookService

# logger = logging.getLogger(__name__)


# class BookAPI:

#     @staticmethod
#     def get(*, book_id: uuid.UUID) -> Dict:
#         logger.info('method "get" called')
#         return BookService.get_book(id=book_id)

# APIs must be used as the entry point for all other consumers who wish to use this domain.
# APIs should own presentational logic and schema declarations.
# Internal domain-to-domain APIs should just be functions.
# You can group internal API functions under a class if it makes sense for organisation.
# If you are using a class for your internal APIs, it must use the naming convention MyDomainAPI.
# Internal functions in APIs must use type annotations.
# Internal functions in APIs must use keyword arguments.
# You should log API function calls.
# All data returned from APIs must be serializable.
# APIs must talk to Services to get data.
# APIs must not talk to Models directly.
# APIs should do simple logic like transforming data for the outside world, or taking external data and transforming it for the domain to understand.
# Objects represented through APIs do not have to map directly to internal database representations of data.

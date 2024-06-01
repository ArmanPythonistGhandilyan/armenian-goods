# # - interfaces.py - Integrations with other domains or external services.

# Interfaces
# Your domain may need to communicate with another domain. 
# That domain can be in another web server across the web, or it could be within the same server. 
# It could even be a third-party service. When your domain needs to talk to other domains, 
# you should define all interactions to the other domain in the interfaces.py file. Combined with APIs (see above), 
# this forms the bounded context of the domain and prevents domain logic from leaking in.

# Consider interfaces.py like a mini Anti-Corruption Layer. 
# Most of the time it won't change and it'll just pass on arguments to an API function. 
# But when the other domain moves - say you extract it into its own web service, 
# your domain only needs to update the code in interfaces.py to reflect the change. No complex refactoring needed, woohoo!

# It's worth noting that some guides would consider this implementation a 'code smell' because it has the potential for creating shallow methods or pass-through methods. This is somewhat true, and leads us back to the pragmatism point in our guide. If you find your interfaces.py is redundant, then you probably don't need it. That said: we recommend starting with it and removing it later.

# An interfaces.py may look like:

# import uuid
# from typing import Dict, Str  # noqa

# # Could be an internal domain or an HTTP API client - we don't care!
# from src.authors.apis import AuthorAPI


# # plain example
# def update_author_name(*, author_name: Str, author_id: uuid.UUID) -> None:
#     AuthorAPI.update_author_name(
#         id=author_id,
#         name=author_name,
#     )


# # class example
# class AuthorInterface:

#     @staticmethod
#     def get_author(*, id: uuid.UUID) -> Dict:
#         return AuthorAPI.get(id=id)

#     @staticmethod
#     def update_author_name(
#       *,
#       author_name: Str,
#       author_id: uuid.UUID,
#     ) -> None:
#         AuthorAPI.update_author_name(
#             id=author_id,
#             name=author_name,
#         )

# The primary components of Interfaces should be functions.
# You can group functions under a class if it makes sense for organisation.
# If you are using a class, it must use the naming convention MyDomainInterface.
# Functions in Interfaces must use type annotations.
# Functions in Interfaces must use keyword arguments.
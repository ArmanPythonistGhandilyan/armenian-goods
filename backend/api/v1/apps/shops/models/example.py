# Models
# Models defines how a data model / database table looks. This is a Django convention that remains mostly unchanged.
# The key difference here is that you use skinny models. No complex functional logic should live here.

# In the past Django has recommended an active record style for its models.
# In practice, we have found that this encourages developers to bloat models.py,
# making it do too much and often binding the presentation and functional logic of a domain too tightly.
# This makes it very hard to have abstract presentations of the data in a domain.
# Putting all the logic in one place also makes it difficult to scale the number of developers working in this part of the codebase.
# See the "Which logic lives where?" section for clarification.

# A models.py file can look like:

import uuid

from django.db import models


class Book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    author_id = models.UUIDField(default=uuid.uuid4)

    @property
    def name_and_publisher(self):
        return f"{self.name}, {self.publisher}"


# Models must not have any complex functional logic in them.
# Models should own informational logic related to them.
# Models can have computed properties where it makes sense.
# Models must not import services, interfaces, or apis from their own domain or other domains.
# Table dependencies (such as ForeignKeys) must not exist across domains. Use a UUID field instead, and have your Services control the relationship between models.
# You can use ForeignKeys between tables in one domain. (But be aware that this might hinder future refactoring.)

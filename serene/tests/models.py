from django.db import models as django_models
from serene import models as serene_models


class DummyModel(serene_models.Model):
    name = serene_models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

class DummierModel(django_models.Model):
    name = django_models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from parler.fields import TranslatedField
from parler.models import TranslatableModel, TranslatedFields, TranslatedFieldsModel


class ManualModel(TranslatableModel):
    shared = models.CharField(max_length=200, default='')

class ManualModelTranslations(TranslatedFieldsModel):
    master = models.ForeignKey(ManualModel, related_name='translations')
    tr_title = models.CharField(max_length=200)


@python_2_unicode_compatible
class SimpleModel(TranslatableModel):
    shared = models.CharField(max_length=200, default='')

    translations = TranslatedFields(
        tr_title = models.CharField(max_length=200)
    )

    def __str__(self):
        return "{0}".format(self.tr_title)


@python_2_unicode_compatible
class AnyLanguageModel(TranslatableModel):
    shared = models.CharField(max_length=200, default='')
    tr_title = TranslatedField(any_language=True)

    translations = TranslatedFields(
        tr_title = models.CharField(max_length=200)
    )

    def __str__(self):
        return "{0}".format(self.tr_title)


@python_2_unicode_compatible
class EmptyModel(TranslatableModel):
    shared = models.CharField(max_length=200, default='')

    # Still tracks how many languages there are, but no actual translated fields exist yet.
    # This is useful when the model is a parent object for inlines. The parent model defines the language tabs.
    translations = TranslatedFields()

    def __str__(self):
        return "{0}".format(self.shared)

import logging
import operator

from django.core.exceptions import ObjectDoesNotExist
from django.db.models.constants import LOOKUP_SEP

logger = logging.getLogger(__name__)


class PropertyField:
    def __init__(self, method):
        self.name = method
        self.verbose_name = method.fget.short_description
        self.internal_type = method.fget.internal_type

    def get_internal_type(self):
        return self.internal_type


class MetaResolver:
    def __init__(self, model):
        self.model = model

    def get_field(self, lookup):
        path = lookup.split(LOOKUP_SEP)
        path, field_name = path[:-1], path[-1]
        model = self.model
        for e in path:
            model = model._meta.get_field(e).related_model
        attr = getattr(model, field_name)
        if isinstance(attr, property):
            return PropertyField(attr)
        return model._meta.get_field(field_name)


class ObjectResolver:
    def __init__(self, object):
        self.object = object

    def get_value(self, lookup):
        try:
            return operator.attrgetter(
                lookup.replace(LOOKUP_SEP, '.'))(self.object)
        except ObjectDoesNotExist:
            return

    def set_value(self, field_name, value):
        try:
            setattr(self.object, field_name, value)
        except AttributeError:
            raise Exception(
                f"Cannot set property {field_name} of "
                f"{self.object.__module__}{self.object.__class__.__name__}")

    def set_values(self, **values):
        for fname, value in values.items():
            self.set_value(fname, value)

    def validate(self, **kwargs):
        self.object.full_clean(**kwargs)

    def save(self):
        self.object.save()

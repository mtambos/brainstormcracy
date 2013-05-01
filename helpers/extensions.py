from datetime import datetime
from helpers.config import datetime_format
from google.appengine.ext.db import Property, DateTimeProperty, Model
from types import MethodType
from collections import namedtuple


def create_property(self, klass,
                    readonly=False,
                    **kwargs):
    prop = klass(**kwargs)
    prop.readonly = readonly
    return prop

setattr(Property, create_property.__name__, MethodType(create_property, Property))


class FormatModel(Model):

    def __new__(cls,
                return_tuple=False,
                **kwargs):
        if return_tuple:
            props = set()
            for name in cls.properties():
                props.add(name)
            props |= set(kwargs.keys())
            props = list(props)
            Model2 = namedtuple('Model2', props)
            return Model2(**{name: (kwargs[name] if name in kwargs else None) for name in props})
        else:
            return Model.__new__(Model, **kwargs)

    def __init__(self,
                from_controller=False,
                **kwargs):
        if from_controller:
            print kwargs
            for name, prop in self.properties().items():
                if name in kwargs and prop.readonly:
                    del kwargs[name]
                else:
                    if name in kwargs\
                            and name in kwargs and kwargs[name] and kwargs[name] != ""\
                            and isinstance(prop, DateTimeProperty)\
                            and not isinstance(kwargs[name], datetime):
                        try:
                            kwargs[name] = datetime.strptime(kwargs[name], datetime_format)
                        except ValueError:
                            raise ValueError("%s, %s, %s" % (str(kwargs), name, kwargs[name]))
        super(FormatModel, self).__init__(**kwargs)

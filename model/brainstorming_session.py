from google.appengine.ext.db import Model, StringProperty, DateTimeProperty, ReferenceProperty


class BrainstormingSession(Model):
    name = StringProperty(required=True)
    doe = DateTimeProperty(auto_now_add=True, verbose_name="Creation Date")
    dou = DateTimeProperty(auto_now=True, verbose_name="Last Update")


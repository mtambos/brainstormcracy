from google.appengine.ext.db import Model, StringProperty, DateTimeProperty, ReferenceProperty, TextProperty
from brainstorming_session import BrainstormingSession


class Idea(Model):
    name = StringProperty(required=True)
    short_description = StringProperty()
    description = TextProperty()
    session = ReferenceProperty(reference_class=BrainstormingSession, collection_name="ideas", required=True)
    doe = DateTimeProperty(auto_now_add=True, verbose_name="Creation Date")
    dou = DateTimeProperty(auto_now=True, verbose_name="Last Update")

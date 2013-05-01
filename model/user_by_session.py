from google.appengine.ext.db import Model, IntegerProperty, StringProperty, DateTimeProperty, ReferenceProperty
from brainstorming_session import BrainstormingSession
from user import User


class UserBySession(Model):
    session = ReferenceProperty(reference_class=BrainstormingSession, collection_name="users", required=True)
    user = ReferenceProperty(reference_class=User, collection_name="sessions", required=True)
    doe = DateTimeProperty(auto_now_add=True, verbose_name="Creation Date")
    dou = DateTimeProperty(auto_now=True, verbose_name="Last Update")

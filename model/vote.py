from google.appengine.ext.db import Model, IntegerProperty, StringProperty, DateTimeProperty, ReferenceProperty
from idea import Idea
from user import User


class Vote(Model):
    idea = ReferenceProperty(reference_class=Idea, collection_name="votes", required=True)
    user = ReferenceProperty(reference_class=User, collection_name="votes", required=True)
    points = IntegerProperty()
    yes_no = StringProperty(choices=["Yes", "No"])
    yes_no_maybe = StringProperty(choices=["Yes", "No", "Maybe"])
    doe = DateTimeProperty(auto_now_add=True, verbose_name="Creation Date")
    dou = DateTimeProperty(auto_now=True, verbose_name="Last Update")

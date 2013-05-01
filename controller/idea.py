from model.idea import Idea as Model
from base import Base


class Idea(Base):
    exposed = True

    def __init__(self):
        super(Idea, self).__init__(Model)

    def GET(self, key=None):
        return super(Idea, self).GET(key)

    def POST(self, **kwargs):
        return super(Idea, self).POST(**kwargs)

    def PUT(self, **kwargs):
        return super(Idea, self).PUT(**kwargs)

    def DELETE(self, key):
        return super(Idea, self).DELETE(key)

from model.vote import Vote as Model
from base import Base


class Vote(Base):
    exposed = True

    def __init__(self):
        super(Vote, self).__init__(Model)

    def GET(self, key=None):
        return super(Vote, self).GET(key)

    def POST(self, **kwargs):
        return super(Vote, self).POST(**kwargs)

    def PUT(self, **kwargs):
        return super(Vote, self).PUT(**kwargs)

    def DELETE(self, key):
        return super(Vote, self).DELETE(key)

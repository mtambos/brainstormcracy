import sys
sys.path.insert(0, 'cherrypy.zip')
from cherrypy import tools, InternalRedirect

from xml.dom.minidom import parseString
import xpath
from datetime import datetime, timedelta

from model.brainstorming_session import BrainstormingSession
from model.idea import Idea
from model.vote import Vote
from model.user import User

TEMPLATE_PATH = "main/"


class Main:
    exposed = True

    @tools.mako(filename=TEMPLATE_PATH + "index.mako")
    def GET(self):
        return []

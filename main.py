import sys
sys.path.insert(0, 'cherrypy.zip')
from cherrypy import tools, config, dispatch, tree

import helpers.decorators
import wsgiref.handlers
from controller.main import Main
from controller.brainstorming_session import BrainstormingSession


#######MAKO###########
tools.mako.collection_size = 500
tools.mako.directories = ["template"]
config["tools.encode.on"] = True
config["tools.encode.encoding"] = "utf-8"

#######ROUTES#########
conf = {
    '/': {
        'request.dispatch': dispatch.MethodDispatcher(),
    }
}
tree.mount(Main(), "/", conf)
tree.mount(BrainstormingSession(), "/session", conf)
wsgiref.handlers.CGIHandler().run(tree)

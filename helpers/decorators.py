'''
Created on Aug 18, 2011

@author: fumanchu
@contributors: hiddenharmony@gmail.com
'''
import sys
sys.path.insert(0, 'cherrypy.zip')
sys.path.insert(0, 'mako.zip')
import cherrypy
from mako.lookup import TemplateLookup
from mako import exceptions

cherrypy.tools.mako = None


class MakoHandler(cherrypy.dispatch.LateParamPageHandler):
    """Callable which sets response.body."""

    def __init__(self, template, next_handler):
        self.template = template
        self.next_handler = next_handler

    def __call__(self):
        try:
            env = globals().copy()
            env.update(self.next_handler())
            return self.template.render(**env)
        except cherrypy.HTTPRedirect:
            raise
        except:
            print exceptions.html_error_template().render()


class MakoLoader(object):

    def __init__(self):
        self.lookups = {}

    def __call__(self, filename,
                 directories=None,
                 module_directory=None,
                 collection_size=None):

        if not directories:
            directories = cherrypy.tools.mako.directories

        if not collection_size and not cherrypy.tools.mako.collection_size:
            collection_size = -1
        elif not collection_size and cherrypy.tools.mako.collection_size:
            collection_size = cherrypy.tools.mako.collection_size
        # Find the appropriate template lookup.
        key = (tuple(directories), module_directory)
        try:
            lookup = self.lookups[key]
        except KeyError:
            lookup = TemplateLookup(directories=directories,
                                    module_directory=module_directory,
                                    collection_size=collection_size,
                                    )
            self.lookups[key] = lookup
        cherrypy.request.lookup = lookup

        # Replace the current handler.
        try:
            cherrypy.request.template = t = lookup.get_template(filename)
            cherrypy.request.handler = MakoHandler(t, cherrypy.request.handler)
        except cherrypy.HTTPRedirect:
            raise
        except:
            print exceptions.html_error_template().render()


makoLoader = MakoLoader()
cherrypy.tools.mako = cherrypy.Tool('on_start_resource', makoLoader)


def http_methods_allowed(methods=['GET', 'HEAD']):
    method = cherrypy.request.method.upper()
    if method not in methods:
        cherrypy.response.headers['Allow'] = ", ".join(methods)
        raise cherrypy.HTTPError(405)

cherrypy.tools.allow = cherrypy.Tool('on_start_resource', http_methods_allowed)

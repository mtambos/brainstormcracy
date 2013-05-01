import sys
sys.path.insert(0, 'mako.zip')
sys.path.insert(0, 'cherrypy.zip')  
import re

from cherrypy import tools
from mako.template import Template
from mako.lookup import TemplateLookup


first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def convert(name):
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def serve_template(templatename, **kwargs):
    templatename = convert(templatename)
    mylookup = TemplateLookup(directories=tools.mako.directories)
    mytemplate = mylookup.get_template(templatename)
    return mytemplate.render(**kwargs)


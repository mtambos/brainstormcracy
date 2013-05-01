'''
Created on Aug 23, 2011

@author: Mario Tambos
'''
import sys
sys.path.insert(0, 'mako.zip')
import re
from mako.runtime import supports_caller

pattern = re.compile('([A-Z][A-Z][a-z])|([a-z][A-Z])')

@supports_caller
def spaceOutCamelCase(dummy, stringAsCamelCase):
    """Adds spaces to a camel case string.  Failure to space out string returns the original string.
    >>> spaceOutCamelCase('DMLSServicesOtherBSTextLLC')
    'DMLS Services Other BS Text LLC'
    """
    
    if stringAsCamelCase is None:
        return None

    return pattern.sub(lambda m: m.group()[:1] + " " + m.group()[1:], stringAsCamelCase)

from google.appengine.api import memcache
import logging
from pytz import timezone
    
def getTimezone(tzname):
    try:
        tz = memcache.get("tz:%s" % tzname)
    except:
        tz = None
        logging.debug("timezone get failed: %s" % tzname)
    if tz is None:
        tz = timezone(tzname)
        memcache.add("tz:%s" % tzname, tz, 86400)
        logging.debug("timezone memcache added: %s" % tzname)
    else:
        logging.debug("timezone memcache hit: %s" % tzname)
    
    return tz

def flattenLists(items):
    retVal = []
    map(lambda x: retVal.extend(x), items)
    return retVal 

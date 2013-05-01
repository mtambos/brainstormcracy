import sys
sys.path.insert(0, 'cherrypy.zip')
import cherrypy
from helpers.auth import *


class AuthController:

    def on_login(self, username):
        """Called on successful login"""

    def on_logout(self, username):
        """Called on logout"""

    def get_loginform(self, username, msg="Enter login information", from_page="/"):
        return """<html><body>
            <form method="post" action="/auth/login">
            <input type="hidden" name="from_page" value="%(from_page)s" />
            %(msg)s<br />
            Username: <input type="text" name="username" value="%(username)s" /><br />
            Password: <input type="password" name="password" /><br />
            <input type="submit" value="Log in" />
        </body></html>""" % locals()

    @cherrypy.expose
    def login(self, username=None, password=None, from_page="/"):
        if username is None or password is None:
            return False

        error_msg = check_credentials(username, password)
        if not error_msg:
            cherrypy.session.regenerate()
            cherrypy.session[SESSION_KEY] = cherrypy.request.login = username
            self.on_login(username)
            return True

    @cherrypy.expose
    def logout(self, from_page="/"):
        sess = cherrypy.session
        username = sess.get(SESSION_KEY, None)
        sess[SESSION_KEY] = None
        if username:
            cherrypy.request.login = None
            self.on_logout(username)
            return True

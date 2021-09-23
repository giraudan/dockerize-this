from datetime import datetime

import cherrypy


class BackEnd:

    @cherrypy.expose
    def index(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

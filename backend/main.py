import os.path
import cherrypy
from backend import BackEnd

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0'
    })
    web_app = BackEnd()
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        }
    }
    cherrypy.quickstart(web_app, '/', conf)

import os.path

import cherrypy

import config
from webapp import WebApp

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8099})
    web_app = WebApp(config)
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        }
    }
    cherrypy.quickstart(web_app, '/', conf)

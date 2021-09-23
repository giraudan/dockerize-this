import cherrypy
import requests as req


def page_template(txt):
    return f"""
    <html>
    <head><title>dockerize-this</title></head>
    <body>
    <p>The time now is {txt}</p>
    </body>
    """


class WebApp:

    def __init__(self, config_opts):
        self.backend_url = "http://" + ":".join([config_opts.BACKEND_HOST, str(config_opts.BACKEND_PORT)])

    @cherrypy.expose
    def index(self):
        r = req.get(self.backend_url)
        return page_template(r.text)

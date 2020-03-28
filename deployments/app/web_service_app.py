import cherrypy
import json
from datetime import datetime

# webServiceApp which returns the current time
class webServiceApp:

    # cherrypy.expose will expose date as an enpoint
    @cherrypy.expose
    # To automatically encode the content of a response using JSON
    @cherrypy.tools.json_out()
    def date(self):
        d = {}
        d['date'] = datetime.now().__str__()
        return d

# To configure the servers use the cherrypy.config.update() method
# The server.socket_host option in this example determines on which network interface CherryPy will listen. 
# The server.socket_port option declares the TCP port on which to listen.    
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0', 'server.socket_port': 7777}
    cherrypy.config.update(config)
    cherrypy.quickstart(webServiceApp())
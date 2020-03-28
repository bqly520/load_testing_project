import requests
import time
import cherrypy

# Time to last byte is the time it takes for the client to receive ALL content of the response.
def getRequests(num):

    # Edge cases, less than 0 and floating numbers. Letters are forbidden from the input type
    if num <= 0 or isinstance(num, float):
        return '<span style="font-family:Arial">Please enter a valid positive integer</span>'

    # Initializing start time, success, failure, TTLB
    start = time.time()
    success = 0
    failure = 0
    TTLB = 0.0

    # Loops to see if current time is less than 1 second + original script start time
    while (time.time() < start + 1): 

        # try/except block to catch any API exceptions from GET request
        try:
            response = requests.get('http://date-time-api:7777/date')
            success = success + 1
            TTLB = TTLB + response.elapsed.total_seconds()
        except Exception:
            failure = failure + 1
        finally:
            if (success+failure) == num:
                break

    # Returns number of success, failres, and average TTLB(if any)
    return ''.join(["<span style='font-family:Arial'>success: ", str(success),"<br/>failure: ",str(num-success),"<br/>avg TTLB: N/A" if success==0 else "<br/>avg TTLB: "+str(round((TTLB/success),5))+"seconds","</span>"])

# Class UIGenerator to create the HTML form to input X API calls per second
class UIGenerator(object):

    # HTML form
    @cherrypy.expose
    def index(self):
        return """<html>
            <head></head>
            <body>
            <form method="get" action="generate">
                <input type="number" value="0" name="numapi" />
                <button type="submit">Enter number of API calls per a second!!</button>
            </form>
            </body>
        </html>"""

    # generate function is called after submit button
    @cherrypy.expose
    def generate(self, numapi):
        return getRequests(int(numapi))

# Start of the script, application hosted on 0.0.0.0 which means all IPv4 addresses for the local machine
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0', 'server.socket_port': 8888}
    cherrypy.config.update(config)
    cherrypy.quickstart(UIGenerator())
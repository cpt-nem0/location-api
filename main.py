""" main module to run the application """
import sys

import uvicorn

from api import app

HOST = "0.0.0.0"
PORT = 5000
DEBUG = False


if __name__ == "__main__":
    if '--host' in sys.argv:
        HOST = sys.argv[sys.argv.index('--host') + 1]
    if '--port' in sys.argv:
        PORT = sys.argv[sys.argv.index('--port') + 1]
    if '--debug' in sys.argv:
        DEBUG = True
    
    uvicorn.run(app, host=HOST, port=PORT, debug=DEBUG)

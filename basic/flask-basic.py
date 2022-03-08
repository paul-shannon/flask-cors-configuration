from flask import Flask
from flask_cors import CORS
app = Flask(__name__, static_url_path='/static')
CORS(app)
# try this: cors.init_app(app, resources={r"*": {"origins": "*"}})
import logging
logging.getLogger('flask_cors').level = logging.DEBUG

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, HEAD"
    response.headers["Access-Control-Expose-Headers"] = "Content-Length, Content-Type, Content-Range"
    response.headers["Accept-Ranges"] = "bytes"
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Vary'] = "*"
    return response

@app.route('/')
def serveStaticFiles():
    return '<h1>CORS and byte-range request flask webserver for igvR and igvShiny (mar 202)</h1>\n'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='60050')

from flask import Flask
from flask_restful import Api
from resources.home import Home
from secure import SecureHeaders

secure_headers = SecureHeaders()

app = Flask(__name__)
api = Api(app)


@app.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    return response


api.add_resource(Home, '/')

if '__main__' == __name__:
    app.run(port=5000, debug=True)
    
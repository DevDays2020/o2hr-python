import logging
from flask import Flask, request, redirect, session

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    """ The app's main page.
    """
    return "<h>This is O2+HR Trend Detection Service Engine</h>"


# start the app
if '__main__' == __name__:
    import flaskbeaker
    flaskbeaker.FlaskBeaker.setup_app(app)

    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, port=8000)
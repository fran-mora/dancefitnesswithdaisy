import random
import sys
import time

# from postediting import find_match

sys.path.append('..')

from flask import Flask, session, send_from_directory
from flask import render_template
import util
from flask import request
# creates a Flask application, named app
app = Flask(__name__)


# a route where we will display a welcome message via an HTML template
@app.route("/")
def index():
    return render_template('index.html')



# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

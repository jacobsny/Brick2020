from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import threading
import time

from backend.searchAPI import valid_search, search_results

app = Flask(__name__)

@app.route("/")
def visual():
    print("Insert HTML HERE")
    # TODO serve Spence's front end html


@app.route('/search', methods=['POST', 'GET'])
def searching():
    error = None
    if request.method == 'POST':
        keywords = request.form["keywords"]
        if valid_search(keywords):
            return search_results(keywords)
        else:
            error = 'Invalid search'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

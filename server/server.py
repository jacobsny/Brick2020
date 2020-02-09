from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import threading
import time

from backend.searchAPI import valid_search, search_results

app = Flask(__name__, template_folder="../frontend/html", static_folder="../frontend/css")

@app.route("/")
def visual():
    return render_template("index.html")
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
    app.run(host="localhost", port=8080, debug=True)

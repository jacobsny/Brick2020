from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import threading
import time

from backend.searchAPI import valid_search, search_results

app = Flask(__name__)

client = MongoClient(port=27017)

@app.route("/")
def visual():
    print("Insert HTML HERE")
    # TODO serve Spence's front end html


@app.route('/search', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        keywords = request.form["keywords"]
        servings = request.form["servings"]
        if valid_search(keywords):
            return search_results(keywords,servings)
        else:
            error = 'Invalid search'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('search.html', error=error)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)

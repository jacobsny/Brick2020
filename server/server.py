from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import threading
import time

from backend.searchAPI import valid_search, search_results, stats_product, stats_cocktails

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
            # TODO choose search results return type
            return search_results(keywords)
        else:
            error = 'Invalid search'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('404.html')


@app.route('/send_stats', methods=['POST', 'GET'])
def stats():
    error = None
    if request.method == 'POST':
        type = request.form["type"] # true is product
        name = request.form["name"]
        if(type):
            stats_product(name)
        else:
            stats_cocktails(name)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('404.html')

@app.route('/get_stats', methods=['POST', 'GET'])
def stats():
    error = None
    if request.method == 'POST':
        type = request.form["type"] # true is product
        name = request.form["name"]
        if(type):
            get_stats_product(name)
        else:
            get_stats_cocktails(name)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)

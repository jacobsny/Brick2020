from flask import Flask, request, render_template
from pymongo import MongoClient
import json
import threading
import time

from backend.searchAPI import valid_search, search_results, stats_product, stats_cocktails, get_stats_product, \
    get_stats_cocktails

app = Flask(__name__, template_folder="../frontend/html", static_folder="../frontend/static")


@app.route("/")
def visual():
    return render_template("index.html")
    # TODO serve Spence's front end html


@app.route("/catalog")
def serve_catalog():
    return render_template("catalog.html")


@app.route("/drunky")
def serve_drunky():
    return render_template("drunky.html")


@app.route("/results")
def serve_results():
    return render_template("results.html")


@app.route("/search")
def serve_search():
    return render_template("search.html")


@app.route('/searching', methods=['POST', 'GET'])
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
def send_stats():
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
def get_stats():
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
    app.run(host="0.0.0.0", port=80, debug=True)
from flask import Flask, request, render_template, jsonify
import backend.wegmans as weg

import backend.otherIngredients as ingred

from pymongo import MongoClient
import json
import threading
import time

from backend.searchAPI import valid_search, search_results, stats_product, stats_cocktails, get_stats_product, \
    get_stats_cocktails, get_random, search_all
from backend.texting import send_ingredients

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


@app.route("/drunkyresult")
def server_rand_result():
    return render_template("drunkyresult.html")


@app.route("/cocktail")
def cocktail_template():
    return render_template("cocktail.html")


@app.route('/searching', methods=['POST', 'GET'])
def searching():
    error = None
    if request.method == 'POST':
        # print("isPost")
        keywords = request.form["keywords"]
        if valid_search(keywords):
            # print(keywords + "-- valid")
            # TODO choose search results return type
            result = search_results(keywords)
            # print(result)
            return jsonify(result)
        else:
            return jsonify({"invalid": keywords})
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
            return jsonify(get_stats_product(name))
        else:
            return jsonify(get_stats_cocktails(name))
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('404.html')


@app.route('/random', methods=["GET"])
def random():
    cocktail = get_random()

    #ingredientPrices = ingred.ingredientPrices(cocktail)

    return jsonify(cocktail)


@app.route("/text", methods=["POST", "GET"])
def texting():
    error = None
    if request.method == 'POST':
        number = request.form["number"]
        provider = request.form["provider"]
        ingredients = request.form["ingredients"]
        send_ingredients(ingredients, provider, number)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('404.html')


@app.route("/catelog")
def catelog():
    return jsonify(search_all())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

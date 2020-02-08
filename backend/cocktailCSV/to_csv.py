import csv
import requests
import json


def get_drinks():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    all_drinks = []
    for letter in alphabet:
        drinks_letter = json.loads(requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=" + letter).text)
        if drinks_letter["drinks"] is not None:
            for drink in drinks_letter["drinks"]:
                all_drinks.append(drink)
    return all_drinks


def to_csv(all_drinks):
    with open("/home/jacobsny/PycharmProjects/Brick2020/data/cocktails.csv", "w", newline='') as cocktails:
        writer = csv.writer(cocktails, delimiter=',')
        writer.writerow(['Name', "Category", "Glass"] + ["Ingredient" + str(i) for i in range(1, 16)] + ["Directions", "isAlcoholic", "Video"])
        for drink in all_drinks:
            writer.writerow([drink["strDrink"], drink["strCategory"], drink["strGlass"]] +
                            [(drink["strIngredient" + str(i)], drink["strMeasure" + str(i)]) for i in range(1, 16)] +
                            [drink["strInstructions"], drink["strAlcoholic"] == "Alcoholic", drink["strVideo"]])
    return


if __name__ == '__main__':
    to_csv(get_drinks())
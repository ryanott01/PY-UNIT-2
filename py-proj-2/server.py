from flask import Flask, render_template, redirect, url_for
from icecreams import find_icecream, get_icecreams, add_icecream_dictionary, write_new_csv


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", icecreams = get_icecreams("icecreams.csv"))
    
@app.route("/order_screen")
def order_screen():
    return render_template("order_screen.html", icecreams = get_icecreams("icecreams.csv"))

@app.route("/order")
def order():
    return render_template("order.html", icecreams = get_icecreams("order.csv"))

@app.route("/add-icecream/<name>")
def add_icecream(name):
    icecream = find_icecream("icecreams.csv", name)

    if icecream:
        add_icecream_dictionary("order.csv", icecream)
        return redirect(url_for("order_screen"))
    else:
        return "Sorry icecream not found."
    

@app.route("/icecream_individual/<name>")
def individual_icecream(name):
    i =  find_icecream("icecreams.csv", name)
    return render_template("individual_icecream.html", icecream = i)


@app.route("/reset_cart")
def reset_cart():
    blank = write_new_csv("order.csv", "epic")
    return render_template("order.html", icecreams = get_icecreams("order.csv"))

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8001, host = "localhost")
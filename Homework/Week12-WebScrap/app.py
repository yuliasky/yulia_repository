from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection


app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    scrape_results = mongo.db.scrape_results.find_one()
    return render_template("index.html", scrape_results=scrape_results)

@app.route("/scrape")
def scraper():
    scrape_results = mongo.db.scrape_results
    scrape_results_data = scrape_mars.scrape()
    scrape_results.update({}, scrape_results_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template, request
from world import getCountryNames , getCountryData

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    countries = getCountryNames()
    countryData = None
    if request.method == "POST":
        country = request.form.get("country")
        countryData = getCountryData(country)
    return render_template("index.html", countries=countries, countryData=countryData)




app.run(debug=True)

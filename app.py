from flask import Flask, render_template, request
from world import getCountryNames , getCountryData, filtrarPaises

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    countries = getCountryNames()
    countryData = None
    if request.method == "POST":
        country = request.form.get("country")
        countryData = getCountryData(country)
    return render_template("index.html", countries=countries, countryData=countryData)


@app.route('/pagina2',methods=["GET","POST"])
def pagina2():
    listaOpciones = ["GDP","Population","Life expectancy","Land Area(Km2)"]
    paisesQueCumplen = None
    if request.method == "POST":
        variable = request.form.get("opcionesVariables")
        min_value = request.form.get("min_value")
        max_value = request.form.get("max_value")

        paisesQueCumplen = filtrarPaises(variable, min_value, max_value)

    return render_template("pagina2.html", listaOpciones=listaOpciones, paisesQueCumplen=paisesQueCumplen)



app.run(debug=True)

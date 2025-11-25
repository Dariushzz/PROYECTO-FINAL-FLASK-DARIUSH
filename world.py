
def buildCountryList():
    file = open('./assets/world-data-2023-CLEAN.csv','r',encoding='utf-8')
    dataset = file.read()
    file.close()
    filas = dataset.split('\n')
    encabezado, *registros = filas
    columnas = encabezado.split(',')

    countryData = []
    for registro in registros:
        infoPais = registro.split(',')
        pais = {}
        for columna,dato in zip(columnas,infoPais):
            pais[columna] = dato
        countryData.append(pais)
    
    return countryData

countryData = buildCountryList()


def getCountryData(country):
    paises = buildCountryList()
    for pais in paises:
        if(pais["Country"]== country):
            return pais
        
# print(getCountryData("Spain"))


def getCountryNames():
    paises = buildCountryList()
    nombrePaises = []
    for pais in paises:
        nombrePaises.append(pais["Country"])
    return nombrePaises


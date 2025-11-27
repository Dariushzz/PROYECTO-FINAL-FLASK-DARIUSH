
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
            dato = dato.strip()
             
            if columna=='GDP':
                dato = dato.replace("$","")

                if (dato==""):
                    dato = 0
                else:
                    dato=int(dato)

            elif columna=='Population':
                if (dato==""):
                    dato = 0
                else:
                    dato=int(dato)

            elif columna=='Life expectancy':
                if (dato==""):
                    dato = 0
                else:
                    dato=float(dato)

            elif columna=='Land Area(Km2)':
                if (dato==""):
                    dato = 0
                else:
                    dato=int(dato)

            pais[columna]=dato
        countryData.append(pais)
    
    return countryData

# result = buildCountryList()
# print(result)

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



    

def filtrarPaises(variable, min_value, max_value):
    paises = buildCountryList()
    PaisesAMostrar= []
    mensajeError = "ERROR: mínimo mayor que máximo"

    min_value=float(min_value)
    max_value=float(max_value)

    if min_value < max_value:

        for pais in paises:
            if pais[variable] >= min_value and pais[variable]<= max_value:
                PaisesAMostrar.append(pais["Country"])
        return PaisesAMostrar
    
    else: return mensajeError

    
# print(filtrarPaises('Population',1366417752, 1366417754))


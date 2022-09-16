#1. Actualizar valores en diccionarios y listas

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#a. Cambia el valor 10 en x a 15
x[1][0] = 15
print(x)
#b. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'
estudiantes[0]['last_name'] = "Bryant"
print(estudiantes[0])
#c. En el directorio_deportes, cambia "Messi" por "Andrés"
directorio_deportes['fútbol'][0] = "Andrés"
print(directorio_deportes['fútbol'])
#d. Cambia el valor 20 en z a 30
z[0]['y'] = 30
print(z)

#2. Iterar a través de una lista de diccionarios

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary():
    lista = []
    for lista in estudiantes:
        print(lista)

iterateDictionary()

#3. Obtener valores de una lista de diccionarios

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(clave, diccionario):
    for i in range(len(diccionario)):
        for key,value in diccionario[i].items():
            if key == clave:
                print(value)

iterateDictionary2('first_name', estudiantes)

#4. Iterar a través de un diccionario con valores de lista

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(key):
    for key, value in dojo.items():
        print(len(value), key)
        print(value)

printInfo('ubicaciones')
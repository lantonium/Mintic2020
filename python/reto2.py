#def calcular_promedio_y_cuadro_honor(grupo):
grupo = [
{'cedula': '00014301503','nombre': 'Pepito', 'nota': '4.3'}, 
{'cedula': '1037678471','nombre': 'Fulanito', 'nota': '3.2'},
{'cedula': '71023567','nombre': 'Pancho', 'nota': '5'},
{'cedula': '32276123','nombre': 'Rita',  'nota': '4.7'},
{'cedula': '1036765245','nombre':'Anita', 'nota': '4.7'},
{'cedula': '89122456','nombre': ' Pedrito', 'nota': '4.7'},
{'cedula': '289765345','nombre': 'Mat', 'nota': '4.8'},
{'cedula': '4576890','nombre': 'Dan', 'nota': '4.8'}]
grupo.sort(key=lambda p: p['nota'], reverse=True)
index = 0
valor = 0
cedulas = []
notas = []
promedio = ""
prom = {}
cuadro ={}
uno = []
dos = []
tres = []

while index < len(grupo):
    for key in grupo[index]:
        if key == 'cedula':
            valor = (grupo[index][key])
            if uno == []:
                uno.append(valor)
            elif dos == [] or index <=2:
                dos.append(valor)
            elif tres == [] or index >2 and index <= 5:
                tres.append(valor)
            if cedulas == None:
                cedulas = valor
            elif cedulas == cedulas.append(valor):
                print(cedulas)
        elif key == 'nota':
            valor = grupo[index][key]
            if notas == None:
                notas = valor
            elif notas == notas.append(float(valor)):
                print(notas)
    index += 1
promedio = sum(notas)/float(len(notas))

lista = {1: uno, 2: dos, 3: tres}
diccionario = dict(lista)
cuadro = (promedio, diccionario)
print(cuadro)

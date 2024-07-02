import json

def borrar_ultimo_caracter(cadena: str):
    cadena_r = ""
    for i in range(len(cadena)-1):
        cadena_r += cadena[i]
    return cadena_r

def scoreboard_carga_datos() -> list:
    with open('ProyectoGAME/scoreboard.json', 'r') as w:
        datos = json.load(w)
    return datos 

def scoreboard_guardar_datos(lista: list):
    with open(f'ProyectoGAME/scoreboard.json', "w") as file:
        json.dump(lista, file, indent= 4, ensure_ascii= False)

def bubble_sort_puntaje(datos):
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            if datos[i]['puntaje'] < datos[j]['puntaje']:
                aux = datos[i]
                datos[i] = datos[j]
                datos[j] = aux
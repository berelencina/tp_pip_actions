import requests

def obtener_dato():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos["title"]
    return "No se pudo obtener el dato"

if __name__ == "__main__":
    resultado = obtener_dato()
    print(resultado)
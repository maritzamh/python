from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Lista de nombres
nombres = ["Juan", "María", "Pedro", "Rosa", "Alvaro"]

# Definir un endpoint para obtener la lista de nombres
@app.get("/nombres", response_class=HTMLResponse)
async def obtener_nombres():
    # Crear una cadena HTML con formato personalizado
    html_content = """
    <html>
    <head>
        <title>Lista de Nombres</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                padding: 20px;
            }
            h1 {
                color: #333333;
            }
            ul {
                list-style-type: none;
                padding: 0;
            }
            li {
                background-color: #ffffff;
                padding: 10px;
                margin-bottom: 5px;
                border-radius: 5px;
                box-shadow: 2px 2px 5px #888888;
            }
        </style>
    </head>
    <body>
        <h1>Lista de Nombres</h1>
        <ul>
    """

    # Agregar cada nombre a la lista HTML
    for nombre in nombres:
        html_content += f"<li>{nombre}</li>"

    # Cerrar las etiquetas HTML
    html_content += """
        </ul>
    </body>
    </html>
    """

    return html_content
#4. Ejecutar la aplicación:
if __name__ == "__main__": 
  import uvicorn 
  uvicorn.run(app, port=3000)

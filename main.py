from fastapi import FastAPI

app = FastAPI()

@app.post("/ejemplo")
async def ejemplo(data: dict):
    """Ejemplo de endpoint que recibe datos en formato JSON"""
    print(data)
    return {"mensaje": "Datos recibidos correctamente"}

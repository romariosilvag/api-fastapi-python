### API con FASTAPI (Python)

Para montar tu proyecto FastAPI en Google App Engine (GAE), sigue estos pasos:

Crea un proyecto en Google Cloud Platform y habilita la facturación si aún no lo has hecho.

Instala el SDK de Cloud y asegúrate de haber iniciado sesión en la cuenta de Google Cloud en tu terminal.

Crea un archivo **requirements.txt** en la raíz de tu proyecto que contenga las dependencias de Python necesarias para tu proyecto, por ejemplo:

```bash
anyio==3.6.2
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
colorama==0.4.6
fastapi==0.95.0
h11==0.14.0
idna==3.4
importlib-metadata==6.1.0
pydantic==1.10.7
requests==2.28.2
sniffio==1.3.0
starlette==0.26.1
typing-extensions==4.5.0
urllib3==1.26.15
uvicorn==0.21.1
zipp==3.15.0
```

Crea un archivo **app.yaml** en la raíz de tu proyecto con la siguiente configuración:

```python
runtime: python38

entrypoint: uvicorn main:app --host=0.0.0.0 --port=${PORT:-8080}

handlers:
- url: /.*
  script: auto

```

En esta configuración, estamos especificando el tiempo de ejecución de Python, el comando de entrada para iniciar nuestra aplicación FastAPI con Uvicorn y cómo manejar las solicitudes HTTP entrantes.

Asegúrate de que tu aplicación tenga una función principal llamada app en un archivo main.py. Aquí hay un ejemplo:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/ejemplo")
async def ejemplo(data: dict):
    """Ejemplo de endpoint que recibe datos en formato JSON"""
    print(data)
    return {"mensaje": "Datos recibidos correctamente"}

```

Despliega la aplicación en App Engine ejecutando el siguiente comando en tu terminal desde la raíz de tu proyecto:

```bash
gcloud app deploy
```

Este comando compilará e implementará tu aplicación en App Engine. Después de unos minutos, podrás acceder a tu aplicación en la URL https://NOMBRE-DEL-PROYECTO.REGION.r.appspot.com.

Nota: Reemplaza "NOMBRE-DEL-PROYECTO" y "REGION" por los valores correctos de tu proyecto y la región en la que se encuentra tu aplicación.

¡Listo! Con esto puedes probar tu aplicación montada en App Engine. Puedes enviar solicitudes HTTP a tu API y ver los resultados en los registros de la consola de GAE.

Para ver los logs en consola puedes utilizar este comando
```bash
  $ gcloud app logs tail -s default
```

Para ver la aplicacion en el navegador
```bash
  $ gcloud app browse
```

Para hacer pruebas localmente, instalar las siguientes librerias

```bash
pip install fastapi uvicorn

```

Para Iniciar el servidor FastAPI localmente:

```bash
uvicorn mi_api:app --reload

```



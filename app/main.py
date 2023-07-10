from fastapi import FastAPI
from fastapi import Path

app = FastAPI()

@app.get('/')
def hello_devops():
    return {
        'Hi': f"Hello I'm Endy Bermudez, follow me on LinkedIn",
    }


@app.get('/{name}')
def hello_devops(
    name: str = Path(...)
):
    return {
        'greeting': f"Hello {name}",
        'mesagge': f"I'm a microservice developed with the best practices of DevOps",
        'author': "Endy Bermudez",
        'cta': "Follow me on https://www.linkedin.com/in/endyb/"
    }
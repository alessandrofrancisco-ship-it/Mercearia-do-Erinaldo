#para istalar as bibliotecas para criação da API vamos usar
#pip install fastapi , uvicorn

from fastapi import FastAPI
from core.database import engine , Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"mensagem":"Merceária do Erinaldo"}
from datetime import datetime
from typing import Union
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from Models.Models import StudyLog, StudyLogInput

app = FastAPI()


@app.get("/ping")
def read_root():
    print("hola")
    return {"Hello": "World"}




@app.get("/primos/{n_max}")
def primos(n_max: int):
    nums_primos = []
    for number in range(0,n_max):
        if number%2==0:
            nums_primos.append(number)
    return {"Resultado: " : nums_primos}


class User(BaseModel):
    name : str
    curso: int


usuarios = []

@app.post("/users/create")
def usuario(usuario:User):
    usuarios.append(usuario)
    return {"Code:" : "OK"}

@app.get("/users/count")
def num_usuarios():
    return {"Numero de usuarios:" : len(usuarios)}

@app.get("/users/users")
def users():
    return {"Usuarios: ": usuarios}


studyloglist={}
@app.post("/studylog/create")
def studylogcreation(studylog : StudyLogInput):
    uuid_generado = uuid.uuid4()
    register = StudyLog(asignatura=studylog.asignatura, inicio=datetime.now().date(), fin=None, id=uuid_generado)
    studyloglist[uuid_generado] = register
    return {"Code:" : "OK", "ID" : uuid_generado}


@app.post("/studylog/stop/{id}")
def studylogcreation(id : str):
    stop_moement = datetime.now()
    studyloglist[id].fin = stop_moement
    print(studyloglist)
    return {"Code:" : "OK", }


@app.get("/studylog/time/{id}")
def calculatetime(id : str):
    obj = studyloglist[id]
    diferencia = obj.fin - obj.inicio

    # Convertir la diferencia a horas y minutos
    horas = diferencia.days * 24 + diferencia.seconds // 3600
    minutos = (diferencia.seconds % 3600) // 60    
    return {"asignatura": obj.asignatura, "Horas" : horas, "minutos" : minutos, "ID" : id}

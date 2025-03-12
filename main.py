from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def read_root():
    print("hola")
    return {"Hello": "World"}




@app.get("/primos/{n_max}")
def primos(n_max: int):
    for number in range(0,n_max):
        if number%2==0:
            print(number)
    return {"Hello": "World"}


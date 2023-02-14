from typing import Union
from wslService import shutdown_distrobution,run_distrobution
from fastapi import FastAPI
from wslModel import distribution_objects,list_distribution

app = FastAPI()

@app.on_event("startup")
def startup_event():
    global distribution_objects
    distribution_objects=list_distribution()

@app.get("/wsl/api/v1/distribution")
def list_all_distribution():
    return distribution_objects

@app.get("/wsl/api/v1/distribution/{index}")
def list_all_distribution(index:int):
    global distribution_objects
    return distribution_objects[index]

@app.post("/wsl/api/v1/distribution/{index}")
def list_all_distribution(index:int):
    if(distribution_objects[index].status == "Running"):
        distribution_objects[index].status="Stopped"
        shutdown_distrobution(distribution_objects[index].name)
    elif(distribution_objects[index].status == "Stopped"):
        distribution_objects[index].status="Running"
        run_distrobution(distribution_objects[index].name)
     


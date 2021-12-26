from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

dataB = [] #hold the data that user throw at it

class buildingClass(BaseModel): #model for the buildingNum and roomNum
    buildingNum: str
    roomNum: str


@app.get("/")
def root():
    return {"key" : "value"}

@app.get("/buildingNum") #get the data from dataB and poop it out
def get_building():
    return dataB

@app.post("/buildingNum")
def creat_building(buildingNum: buildingClass): #pick up input and put in buildingNum
    dataB.append(buildingNum)                   #put the data into dataB
    return dataB[-1]                            #return the last item

@app.delete("/buildingNum/{buildingID}")    #delete building by taking in index of the array
def delete_building(buildingID: int):
    dataB.pop(buildingID-1)
    return {}

@app.get("/buildingNum/{buildingID}")
def get_building_by_num(buildingID: int):
    return dataB[buildingID-1]

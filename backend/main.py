from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

dataB = [] #hold the data that user throw at it

class buildingClass(BaseModel): #model for the buildingNum and roomNum
    buildingNum: str
    roomNum: list

@app.get("/buildingNum")
def get_building(): #take the data from dataB and return it
    return dataB

@app.post("/buildingNum")
def creat_building(buildingNum: buildingClass): #Creat new object and put it in the last spot
    dataB.append(buildingNum)
    return dataB[-1]
    
@app.get("/buildingNum/{buildingID}")
def get_building_by_index(buildingID: int): #take in int and return building by index
    return dataB[buildingID-1]

@app.get("/buildingNum/{buildingID}/roomNum/{roomID}")
def get_room_by_index(buildingID: int, roomID: int):    #take in building and room int
    return dataB[buildingID-1].roomNum[roomID-1]        #return the room number accordingly

@app.put("/buildingNum/{buildingID}")
def rewrite_room_numbers(buildingID: int, roomEdit: list):  #take in building int and new list of roomNum
    dataB[buildingID-1].roomNum = roomEdit                  #replace the existed list with the new list
    return dataB[buildingID-1]

@app.delete("/buildingNum/{buildingID}")
def delete_building(buildingID: int):   #take in int and match building by index
    dataB.pop(buildingID-1)             #delete the building accordingly
    return {}

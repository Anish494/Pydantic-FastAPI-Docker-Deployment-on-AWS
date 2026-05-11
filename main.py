from fastapi import FastAPI, Path , HTTPException, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import json

app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str, Field(..., description='ID of the patient', examples=['P001', 'P002'])]
    name:Annotated[str, Field(..., description='Name of the patient ')]
    city:Annotated[str, Field(..., description='City where the patient is living')]
    age:Annotated[str, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender:Annotated[Literal['male', 'female', 'others'],  Field(..., description='Gender of the patient')]
    height:Annotated[float, Field(..., gt=0, description='H')]
    weight: float 


def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data 

@app.get("/")
def hello():
    return {
        'message':'Hello World'
    }


@app.get("/about")
def about():
    return{
        'message':'This is about section of the webpage'
    }


@app.get('/view')
def view():
    data=load_data()
    return data 


@app.get('/patient/{patient_id}')
def view_patient(patient_id : str = Path(..., description='ID of patient in DB' , example='P001' )):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'not found'}
    raise HTTPException(status_code=404, detail='Patient not found')


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description = 'Sort on the basis of height, weight or bmi'), order:str =Query('asc', description='sort in asc  or desc order')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select form {valid_fields}')
    
    if order not in ['asc' , 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data=load_data()
    sort_order = True if order == 'desc' else False 
    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by,0) , reverse=sort_order)
    return sorted_data 
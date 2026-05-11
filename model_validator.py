from pydantic import BaseModel , EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional , Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Anish','Amit'])]

    age:int 
    email:EmailStr
    weight:float
    married:bool
    allergies:List[str] 
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model 


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    print('Updated')

patient_data={
    'name':'OmDon', 'age':63, 'email': 'a@hdfc.com' ,'weight':45 ,'married':True  , 'allergies':['mushroom', 'ant'], 'contact_details':{'email':'a@gmail', 'ph_no': '45678', 'emergency':'98989898'}
}

patient1=Patient(**patient_data)
insert_patient_data(patient1)
from pydantic import BaseModel , EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional , Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Anish','Amit'])]

    age:int 
    email:EmailStr
    weight:float
    married:bool
    allergies:List[str] 
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value 
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        name = value.upper()
        return name 

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print('Inserted')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_data={
    'name':'OmDon', 'age':23, 'email': 'a@hdfc.com' ,'weight':45 ,'married':True  , 'allergies':['mushroom', 'ant'], 'contact_details':{'email':'a@gmail', 'ph_no': '45678'}
}

patient1=Patient(**patient_data)
insert_patient_data(patient1)
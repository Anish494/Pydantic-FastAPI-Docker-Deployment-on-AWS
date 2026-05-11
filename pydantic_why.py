from pydantic import BaseModel , EmailStr, AnyUrl, Field
from typing import List, Dict, Optional , Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Anish','Amit'])]

    age:int =Field(gt=0 , lt=120) 
    email:EmailStr
    weight:Annotated[float, Field(gt=0, strict=True)]
    married:Annotated[bool, Field(default=None, description='Is the patient married or unmarried')]
    allergies:Optional[List[str]] = None 
    contact_details:Dict[str,str]

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
    'name':'OmDon', 'age':23, 'email': 'a@gmail.com' ,'weight':45 , 'allergies':['mushroom', 'ant'], 'contact_details':{'email':'a@gmail', 'ph_no': '45678'}
}

patient1=Patient(**patient_data)
insert_patient_data(patient1)
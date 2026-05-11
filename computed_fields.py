from pydantic import BaseModel , EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional , Annotated
class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Anish','Amit'])]

    age:int 
    email:EmailStr
    weight:float
    height:float 
    married:bool
    allergies:List[str] 
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi_value = round(self.weight/(self.height**2),2)
        return bmi_value  


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    print(patient.bmi)
    print('Updated')

patient_data={
    'name':'OmDon', 'age':63, 'email': 'a@hdfc.com' ,'weight':45 , 'height':1.3, 'married':True  , 'allergies':['mushroom', 'ant'], 'contact_details':{'email':'a@gmail', 'ph_no': '45678', 'emergency':'98989898'}
}

patient1=Patient(**patient_data)
insert_patient_data(patient1)
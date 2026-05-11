from pydantic import BaseModel

class Address(BaseModel):
    city:str 
    state:str 
    pincode:str 


class Patient(BaseModel):
    name:str 
    gender: str 
    age:int 
    address : Address

address_details={'city':'ktm', 'state':'Bagmati', 'pincode':'3456'}
address1=Address(**address_details)

patient_dict={ 'name':'Anish', 'gender':'Male' , 'age':78, 'address':address1}
patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.pincode)


# //convert model to dictionary for further processig 
temp = patient1.model_dump()
print(temp)



# //convert model to json for further processig 
# temp = patient1.model_dump_json()
# temp = patient1.model_dump_json(include=['name', 'age'])
temp = patient1.model_dump_json(exclude=['name', 'age'])
print(temp)

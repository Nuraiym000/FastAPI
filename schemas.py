from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"nura",
                "email":"nurajymmm1@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }

class Settings(BaseModel):
    authjwt_secret_key:str='18d4e9785ffd6b5dfe2318c5033dac5bdbaca857409c90068f6f1d0f1fd04812'

class LoginModel(BaseModel):
    username:str
    password:str



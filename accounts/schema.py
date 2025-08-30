from pydantic import BaseModel


# schema for register user
class UserRegisterSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    is_mechanic: bool


# schema for login user
class UserLoginSchema(BaseModel):
    username: str
    password: str
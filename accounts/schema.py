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


# schema for use in other schemas to show user detail
class UserSchema(BaseModel):
    id: int
    username: str

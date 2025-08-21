import uuid

from pydantic import BaseModel, Field, EmailStr


# Добавили модель UserSchema
class UserSchema(BaseModel):
    """
    Модель пользователя
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


# Добавили модель CreateUserRequestSchema
class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса при создании нового пользователя
    """
    email: EmailStr
    password : str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

# Добавили модель CreateUserResponseSchema
class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа с данными созданного пользователя
    """
    user: UserSchema
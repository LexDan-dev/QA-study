from pydantic import BaseModel, ConfigDict, Field, field_validator


class Post(BaseModel):
    model_config = ConfigDict(extra="ignore")

    userId: int = Field(..., gt=0)
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=200)
    body: str = Field(..., min_length=1)

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title не может быть пустым")
        return v.strip()


class Geo(BaseModel):
    model_config = ConfigDict(extra="ignore")

    lat: str
    lng: str


class Address(BaseModel):
    model_config = ConfigDict(extra="ignore")

    street: str = Field(..., min_length=1)
    city: str = Field(..., min_length=1)
    zipcode: str = Field(..., min_length=1)
    geo: Geo


class User(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    username: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    address: Address

    @field_validator("email")
    @classmethod
    def email_has_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("email должен содержать @")
        return v.lower()

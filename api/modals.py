from pydantic import BaseModel


class Address(BaseModel):
    address: str
    output_format: str
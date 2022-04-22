from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    address: str
    output_format: Optional[str] = "json"
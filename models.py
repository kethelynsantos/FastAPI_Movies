from typing import Optional
from pydantic import BaseModel


class Movie(BaseModel):  # Por padrão já herda várias coisas, como validação de dados!
    id: Optional[int] = None  # Já que é opcional
    name: str
    assessment: int
    genre: str
    runtime: str
    phrase: str

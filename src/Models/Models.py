from datetime import date
from uuid import UUID
from typing import Optional
from pydantic import BaseModel


class StudyLog(BaseModel):
    asignatura : str
    inicio : date
    fin : Optional[date]
    id : UUID

class StudyLogInput(BaseModel):
    asignatura : str

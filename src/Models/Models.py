from datetime import date, datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel

class StudyLog(BaseModel):
    asignatura : str
    inicio : datetime
    fin : Optional[datetime]
    id : UUID

class StudyLogInput(BaseModel):
    asignatura : str

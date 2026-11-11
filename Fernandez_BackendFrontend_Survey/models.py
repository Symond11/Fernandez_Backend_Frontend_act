from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name: str
    address :str
    age: str 
    work: str
    civil: str
    love: str
    place_birth : str
    date_birth : str
    time_birth :str




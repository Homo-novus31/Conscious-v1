#schema
from datetime import  datetime,timezone
from dataclasses import dataclass
@dataclass
class RawItem:
    title:str
    source:str
    abstract:str
    url:str
    published_at:datetime
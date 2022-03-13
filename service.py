from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class CV(BaseModel):
    name: str
    age: int
    status: bool
    is_offer: Optional[bool] = None

app = FastAPI()
@app.get("/hello/{my_query}")
def home(my_query, q:Optional[str]=None):
    return{"welcome":"Thanks","user_input":my_query,"query":q}

@app.put("/endpoint")
async def endpoint(resume:CV):
    return{"user_name":resume.name}




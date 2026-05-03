from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()

class Details(BaseModel):
    name: str
    age: int
    place: str

@app.get("/name")
def get_your_name():
    return "Sai natha reddy Nooli"


@app.get("/health")
def health():
    return "App is up and running"

@app.post("/details")
def display_details(details: Details):
    return f"Name:  {details.name} Age: {details.age} Place:  {details.place}"

handler = Mangum(app)
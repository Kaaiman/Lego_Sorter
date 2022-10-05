# Dit draait op Raspberry
from fastapi import FastAPI
from detect_color import detect_color

app = FastAPI()

# start with 
# uvicorn color_recognition:app --reload --host=0.0.0.0
# http://localhost:8000/part-recognition

def detect_part():
    color = detect_color()
    return {"color": color }
 
@app.get("/part-recognition")
async def root():
    return detect_part()

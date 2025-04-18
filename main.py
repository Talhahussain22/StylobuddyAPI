from fastapi import FastAPI
from pydantic import BaseModel
from gradio_client import Client


# Initialize FastAPI app
app = FastAPI()



# Load Gradio model client (replace with your model ID if needed)
client = Client("Talha2005/stylobuddy")

# Input data model
class InputModel(BaseModel):
    shirts: str
    pants: str

# Test route to confirm the API is running
@app.get("/")
def read_root():
    return {"status": "API is running"}

# Prediction route
@app.post("/predict")
def predict(data: InputModel):
    try:
        result = client.predict(
            shirts=data.shirts,
            pants=data.pants,
            api_name="/predict"
        )
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

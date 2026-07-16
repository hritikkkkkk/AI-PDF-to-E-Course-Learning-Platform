from fastapi import FastAPI
from app.routes.upload import router as upload_router

from app.routes.upload import router as upload_router

print("UPLOAD ROUTER IMPORTED")
app = FastAPI(title="AI Course Backend")

app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "AI Course Backend Running"}
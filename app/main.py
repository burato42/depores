import uvicorn
from fastapi import FastAPI

from app.routers.business import business_router

app = FastAPI()


@app.get("/health")
async def root():
    return {"message": "I'm alive"}


app.include_router(business_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)

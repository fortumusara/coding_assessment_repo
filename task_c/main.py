import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()
NODE_ID = os.getenv("NODE_ID", "unknown")

@app.post("/process")
async def process(request: Request):
    body = await request.body()
    result = [str(sum(bytearray(body)))]

    return JSONResponse(content={"id": NODE_ID, "result": result})

#!/usr/local/bin/python3

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello, world'}

if __name__ == '__main__':
    uvicorn.run(app)

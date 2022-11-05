#!/usr/local/bin/python3

"""
'hello, world'を返すサーバ
`pip install fastapi uvicorn`
を事前に実行しておく必要がある
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'hello, world'}

if __name__ == '__main__':
    uvicorn.run(app)

import asyncio

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn

from utils.types import SingleInput, BatchInput, ProcessingOutput
import config
from start_app import EXECUTOR, _initialize_workers


app = FastAPI()


@app.post('/process/batch')
async def process_batch(data: BatchInput):
    try:
        response = {'result': []}
        for text in data.text:
            response['result'].append(await EXECUTOR.process_request(text))

        print(response)
        response_json = jsonable_encoder(response)
        return JSONResponse(content=response_json)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        EXECUTOR.shutdown(wait=False)
        return
    except Exception as err:
        return JSONResponse(content={'error': err.__class__}, status_code=500)


@app.post('/process/single')
async def process_single(data: SingleInput):
    try:
        response = {'result': await EXECUTOR.process_request(data.text)}

        print(response)
        response_json = jsonable_encoder(response)
        return JSONResponse(content=response_json)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        EXECUTOR.shutdown(wait=False)
        return
    except Exception as err:
        return JSONResponse(content={'error': err.__class__}, status_code=500)


if __name__ == '__main__':
    try:
        asyncio.run(_initialize_workers(EXECUTOR, config.WORKERS_COUNT))
        uvicorn.run('main:app', host='0.0.0.0', port=config.APP_PORT)
    except KeyboardInterrupt:
        print('Keyboard interrupt')
        EXECUTOR.shutdown(wait=False)

from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

import util.app_util
from app.test_app import router_test
from model import msg
from model.response import BaseResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_server()
    yield


app = FastAPI(lifespan=lifespan)
app_config = util.app_util.app_config()
app_logger = util.app_util.app_logger()
api_prefix = f"/{app_config.server.api_version}"
app.include_router(router_test, prefix=api_prefix)


@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        content=jsonable_encoder(BaseResponse(
            code=msg.ServerError.code,
            message=msg.ServerError.msg,
            data=exc.__str__())
        ),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        content=jsonable_encoder(BaseResponse(
            code=msg.BadRequest.code,
            message=msg.BadRequest.msg,
            data=exc.__str__())
        ),
    )


def init_server():
    app_logger.info("init server")


def main():
    uvicorn.run(app="main:app", host=app_config.server.host, port=app_config.server.port, workers=2, reload=True)


if __name__ == '__main__':
    main()

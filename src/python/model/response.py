from pydantic import BaseModel

from model.type import TypeJson


class BaseResponse(BaseModel):
    code: int = 0
    message: str = "success"
    data: TypeJson = None

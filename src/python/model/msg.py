

class __CodeMsg:
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg


Success = __CodeMsg(0, "success")

BadRequest = __CodeMsg(400101, "invalid request")

ServerError = __CodeMsg(500101, "internal server error")
Unimplemented = __CodeMsg(500201, "unimplemented")
FormatError = __CodeMsg(500301, "format error")

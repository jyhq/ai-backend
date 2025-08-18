from fastapi import APIRouter

router_test = APIRouter(prefix="/test")


@router_test.get("/hello")
def test():
    return "hello"

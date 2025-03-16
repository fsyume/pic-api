from fastapi import APIRouter
from starlette.responses import RedirectResponse

router = APIRouter()


@router.get("/")
async def jump_blog():
    # 301 永久重定向
    return RedirectResponse("https://www.fsyume.com", status_code=301)

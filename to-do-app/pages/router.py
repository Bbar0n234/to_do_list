from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from api.api_v1.user import get_users


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/admin")
def get_admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})


@router.get("/admin/all_users")
def get_admin_page_users(request: Request, users=Depends(get_users)):
    return templates.TemplateResponse("admin.html", {"request": request, "users": users})
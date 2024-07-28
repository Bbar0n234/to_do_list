from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from api.api_v1.user import get_users
from api.api_v1.task import get_user_tasks


router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/admin")
def get_admin_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/admin/users")
def get_admin_page_users(request: Request, users=Depends(get_users)):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@router.get("/admin/tasks")
def get_admin_page_users(request: Request):
    return templates.TemplateResponse("tasks.html", {"request": request})

@router.get("/admin/tasks/{user_id}")
def get_admin_page_users(request: Request, user_id: int, tasks=Depends(get_user_tasks)):
    return templates.TemplateResponse("user_tasks.html", {"request": request, "tasks": tasks})
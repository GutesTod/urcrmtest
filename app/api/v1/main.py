from fastapi import APIRouter
from modules.users.views import UserViewset

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(UserViewset().get_router())
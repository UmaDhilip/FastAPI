from fastapi import APIRouter

router_app = APIRouter()


@router_app.get("/auth")
async def get_user():
    return { 'User' : 'Authenticated'}
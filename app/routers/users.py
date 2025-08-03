from fastapi import APIRouter

router = APIRouter()


# will keep it for users
@router.get("/", tags=["users"])
async def read_users():
    return {"user1": "Me"}


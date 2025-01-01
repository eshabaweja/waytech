from fastapi import APIRouter

router = APIRouter()

# prefix auth

@router.post("/login")
async def auth_login():
    pass

@router.post("/refresh")
async def auth_refresh():
    pass

@router.post("/logout")
async def auth_logout():
    pass
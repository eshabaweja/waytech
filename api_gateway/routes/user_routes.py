from fastapi import APIRouter

router = APIRouter()

# prefix users

@router.get("/{id}")
async def users_read(id):
    return {"message":f"Reading user {id}..."}

@router.post("")
async def users_create():
    return {"message":f"Creating new user..."}

@router.put("/{id}")
async def users_update(id):
    return {"message":f"Updating user {id}..."}

@router.delete("/{id}")
async def users_delete(id):
    return {"message":f"Deleting user {id}..."}
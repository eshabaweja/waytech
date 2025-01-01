from fastapi import APIRouter

router = APIRouter()

# prefix orders

@router.get("/{id}")
async def orders_read(id):
    return {"message":f"Viewing order {id} from records..."}

@router.post("")
async def orders_create():
    return {"message":f"Created new order..."}

@router.put("/{id}")
async def orders_update(id):
    return {"message":f"Updating order {id} in records..."}

@router.delete("/{id}")
async def orders_delete(id):
    return {"message":f"Deleting order {id} from records..."}
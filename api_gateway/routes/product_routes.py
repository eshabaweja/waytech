from fastapi import APIRouter

router = APIRouter()

# prefix products

@router.get("/")
async def products():
    return {"message":f"Retreiving all product records..."}

@router.get("/{id}")
async def products_read(id):
    return {"message":f"Retreiving product {id} from records..."}

@router.post("")
async def products_create():
    return {"message":f"Creating new product..."}

@router.put("/{id}")
async def products_update(id):
    return {"message":f"Updating product {id} in records..."}

@router.delete("/{id}")
async def products_delete(id):
    return {"message":f"Deleting product {id} from records..."}
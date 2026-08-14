from fastapi import APIRouter

router = APIRouter(prefix="/items",tags=["items"])

@router.get("/")
async def get_all_items():
    pass

@router.get("/{item_id}")
async def get_item(item_id: int):
    pass

@router.post("/")
async def create_item():
    pass

@router.put("/{item_id}")
async def update_item(item_id: int):
    pass


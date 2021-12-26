from typing import Optional

from fastapi import FastAPI

app = FastAPI()



@app.get("/users/{user_id}/items/{items_id}")

async def read_user_item(

        user_id: str, item_id: str, q: Optional[str] = None, short: bool = False

):
    item = {"user_id": user_id, "item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

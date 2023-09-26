from fastapi import FastAPI

my_app = FastAPI()


@my_app.get("/read")
async def read_root():
    return {"message":"Hello Sudeepa"}

@my_app.get("/products")
def okay():
    return ({"Product_id":"123",
            "Product_name":"LGTV",
            "Product_price":12300,
            "Product_availability":"120"},
            {"Product_id":"156",
            "Product_name":"LGTV",
            "Product_price":12300,
            "Product_availability":"120"},
            {"Product_id":"156",
            "Product_name":"LGTV",
            "Product_price":12300,
            "Product_availability":"120"},

            )

@my_app.get("/items/{item_id}")
def read_item(item_id:str):
    return {"item_id":item_id}

from fastapi import FastAPI, APIRouter 

app = FastAPI()

customer = APIRouter(
    prefix="/customer",
    tags=["customer"],
    dependencies=None,
    responses={404: {"error": "Not found"}}
)


@customer.post("/action")
async def customer_action():
    return "ok"


app.include_router(customer)
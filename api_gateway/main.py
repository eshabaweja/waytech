from fastapi import FastAPI
from routes import auth_routes, product_routes, order_routes, user_routes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(product_routes.router, prefix="/products", tags=["Products"])
app.include_router(order_routes.router, prefix="/orders", tags=["Orders"])
app.include_router(user_routes.router, prefix="/users", tags=["Users"])


@app.get("/")
async def root():
    return {"message":"Hello, Cubby!"}

@app.post("/{name}")
async def root(name):
    return {"message":f"Hello, Bubby! I am {name}."}
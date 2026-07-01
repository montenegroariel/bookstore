# main.py
from fastapi import FastAPI
from modules.auth.adapters.router import router as auth_router
from modules.products.adapters.router import router as products_router

app = FastAPI(
    title="Hexagonal Vertical Slicing API",
    description="FastAPI + Clean Architecture + Vertical Slicing",
    version="1.0.0"
)

# Registro de Slices
app.include_router(auth_router)
app.include_router(products_router)

@app.get("/")
def read_root():
    return {"status": "Healthy", "architecture": "Hexagonal Vertical Slicing"}
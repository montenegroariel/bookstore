# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.auth.adapters.router import router as auth_router
from modules.products.adapters.router import router as products_router
from modules.sales.adapters.router import router as sales_router

app = FastAPI(
    title="Hexagonal Vertical Slicing API",
    description="FastAPI + Clean Architecture + Vertical Slicing",
    version="1.0.0"
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173"], # Puerto de Vue.js
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Registro de Slices
app.include_router(auth_router)
app.include_router(products_router)
app.include_router(sales_router)

@app.get("/")
def read_root():
    return {"status": "Healthy", "architecture": "Hexagonal Vertical Slicing"}
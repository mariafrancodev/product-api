from fastapi import FastAPI

from app.routers import products_router as products

app = FastAPI(
    title="Product Detail API",
    description="API serving product detail data for a product detail page (inspired by MercadoLibre)",
    version="0.1.0",
)

app.include_router(products.router)


@app.get("/health")
async def health():
    return {"status": "ok"}

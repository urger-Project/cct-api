from fastapi import FastAPI

from cct_brasil_api.config import get_settings
from cct_brasil_api.routers import health, instruments, unions

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="API aberta para instrumentos coletivos de trabalho do Brasil.",
    debug=settings.app_debug,
)

app.include_router(health.router)
app.include_router(instruments.router)
app.include_router(unions.router)


import urllib3
import uvicorn
from fastapi import FastAPI
from app.api.routers import sample_endpoint
from app.api.routers import healthcheck
from app.api.routers import admin
import app.common.constants as C
from app.common.config import setup_logging, setup_environment


def create_application() -> FastAPI:
    urllib3.disable_warnings()
    setup_environment(common_env_file_path=C.COMMON_ENV_FILE)
    setup_logging(C.DEFAULT_LOGGER)
    app = FastAPI(
        title=C.APP_NAME,
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )
    app.include_router(sample_endpoint.router)
    app.include_router(admin.router)
    app.include_router(healthcheck.router)
    return app


application = create_application()
if __name__ == "__main__":
    """
    For testing purposes.
    
    Run with "python -m app.main" while being in project root.
     
    For production use deployment using Gunicorn as specified in Dockerfile
     
     """
    uvicorn.run("app.main:application", host="0.0.0.0", port=5555, reload=True)

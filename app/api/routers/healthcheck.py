"""
Healthcheck endpoint - often used in Kubernetes to monitor the liveness of containerized APIs
"""
import logging
from fastapi import APIRouter
from starlette import status

import app.common.constants as C

logger = logging.getLogger(C.DEFAULT_LOGGER)
router = APIRouter(
    prefix="/health",
    tags=["healthcheck"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.get("/ready", status_code=status.HTTP_200_OK, name= "ready", include_in_schema=False)
@router.get("/live", status_code=status.HTTP_200_OK, name = "live", include_in_schema=False)
def healthcheck():
    return 1

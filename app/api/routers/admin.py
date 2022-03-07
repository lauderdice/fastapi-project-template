import logging
from fastapi import APIRouter, Depends, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasicCredentials
from starlette import status
from starlette.responses import JSONResponse
import app.common.constants as C
from app.common.models import ErrorResponse
from app.dependencies.security import basic_auth


logger = logging.getLogger(C.DEFAULT_LOGGER)
router = APIRouter(
    prefix="",
    tags=["admin"]
)


@router.get(C.DOCS_URL, include_in_schema=False)
def get_apidoc(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    try:
        if not (credentials.username == C.APIDOC_USERNAME and credentials.password == C.APIDOC_PASSWORD):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        return get_swagger_ui_html(openapi_url=C.OPENAPI_URL, title="API documentation")
    except:
        logger.exception("Exception occured while processing the request")
        err_resp = ErrorResponse(StatusCode=status.HTTP_400_BAD_REQUEST,
                                 ErrorMessage=C.THERE_WAS_PROBLEM_PROCESSING)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=err_resp.dict())


@router.get(C.OPENAPI_URL, include_in_schema=False)
async def openapi(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    try:
        if not (credentials.username == C.APIDOC_USERNAME and credentials.password == C.APIDOC_PASSWORD):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        from app.main import application
        return get_openapi(
            title=application.title,
            version=application.version,
            openapi_version=application.openapi_version,
            routes=application.routes)
    except:
        logger.exception("Exception occured while processing the request")
        err_resp = ErrorResponse(StatusCode=status.HTTP_400_BAD_REQUEST,
                                 ErrorMessage=C.THERE_WAS_PROBLEM_PROCESSING)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=err_resp.dict())

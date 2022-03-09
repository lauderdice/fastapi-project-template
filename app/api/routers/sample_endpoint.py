import logging

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from starlette import status

import app.common.constants as C
from app.api.logic.sample_logic import SampleLogicHandler
from app.common.helpers import is_apikey_valid
from app.common.models import SampleResponse, ErrorResponse, SampleRequest
from app.dependencies.security import api_key_header

logger = logging.getLogger(C.DEFAULT_LOGGER)
router = APIRouter(
    prefix="/sample",
    tags=["sample_endpoint"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@router.post("", response_model=SampleResponse,
            responses={status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse}})
def get_sample_response(request_body: SampleRequest, request_key: str = Depends(api_key_header)):
    if not is_apikey_valid(request_key):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    try:
        handler = SampleLogicHandler()
        response = handler.handle_request(request_body.account)
        return response
    except:
        logger.exception("Exception occured while processing the request")
        err_resp = ErrorResponse(StatusCode=status.HTTP_400_BAD_REQUEST,
                                 ErrorMessage=C.THERE_WAS_PROBLEM_PROCESSING)
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=err_resp.dict())

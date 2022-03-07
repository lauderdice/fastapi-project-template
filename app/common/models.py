"""
File for storing all Pydantic models and @dataclasses
"""

from typing import List
from uuid import UUID

from pydantic import BaseModel

from app.common.enums import SampleCarEnum


class SampleResponse(BaseModel):
    random_words: List[str]
    number: int
    carbrand: SampleCarEnum
    account: UUID

class SampleRequest(BaseModel):
    account: UUID


class ErrorResponse(BaseModel):
    StatusCode: int
    ErrorMessage: str

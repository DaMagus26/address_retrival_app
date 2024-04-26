"""
Type declarations for incoming API requests
"""

from pydantic import BaseModel
from typing import List


class SingleInput(BaseModel):
    text: str


class BatchInput(BaseModel):
    text: List[str]


class ProcessingOutput(BaseModel):
    result: List[List[str] | str]

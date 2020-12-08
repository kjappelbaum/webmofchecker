from typing import Optional
from pydantic import BaseModel, validator
from . import __version__

EXTENSIONS = "cif"


class CheckResponse(BaseModel):
    """Default response for a MOFCheck"""

    checkResults: dict
    expectedResults: Optional[dict]
    checkDescriptions: Optional[dict]
    apiVersion: Optional[str] = __version__


class MOFInput(BaseModel):
    """Input for the check"""

    fileContent: str
    extension: Optional[str] = "cif"

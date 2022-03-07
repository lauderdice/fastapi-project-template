"""
File for storing functionality related to authentication and security
"""

from fastapi.security import APIKeyHeader, HTTPBasic

import app.common.constants as C

api_key_header = APIKeyHeader(name=C.X_API_KEY, auto_error=True)
basic_auth = HTTPBasic()

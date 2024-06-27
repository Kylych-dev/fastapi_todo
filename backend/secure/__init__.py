from fastapi.security import APIKeyHeader
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

apikey_schema = APIKeyHeader(
    name='Authorization',
    auto_error=False
)


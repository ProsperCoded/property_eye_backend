"""
Security utilities for authentication.
"""

from datetime import datetime, timedelta
from typing import Any, Union

from passlib.context import CryptContext
from jose import jwt

from src.core.config import settings

pwd_context = CryptContext(
    schemes=["bcrypt_sha256", "bcrypt"],  # bcrypt_sha256 removes 72-byte password limit
    default="bcrypt_sha256",
    deprecated="auto"
)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Generate a password hash, supporting long passwords via bcrypt_sha256."""
    
    print('password is of type:', type(password), 'length:', len(password), password)
    return pwd_context.hash(password)


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str: # type: ignore
    """Create a JWT access token."""
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {"sub": str(subject), "exp": expire}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

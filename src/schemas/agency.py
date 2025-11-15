"""
Agency Pydantic schemas for API requests and responses.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AgencyBase(BaseModel):
    """Base schema for agency data."""

    name: str = Field(..., min_length=1, max_length=255, description="Agency name")


class AgencyCreate(AgencyBase):
    """Schema for creating a new agency."""

    pass


class AgencyUpdate(BaseModel):
    """Schema for updating an existing agency."""

    name: Optional[str] = Field(
        None, min_length=1, max_length=255, description="Agency name"
    )


class AgencyResponse(AgencyBase):
    """Schema for agency response."""

    id: str = Field(..., description="Unique agency identifier")
    created_at: datetime = Field(..., description="Agency creation timestamp")

    class Config:
        from_attributes = True


class AgencyListResponse(BaseModel):
    """Schema for paginated agency list response."""

    agencies: list[AgencyResponse] = Field(..., description="List of agencies")
    total: int = Field(..., description="Total number of agencies")
    page: int = Field(..., description="Current page number")
    page_size: int = Field(..., description="Number of items per page")

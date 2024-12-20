from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from typing import List, Optional


class ProfileOnlyRead(BaseModel):
    """
    A thin profile model that only includes the profile information and no child objects.
    """

    profile_id: str
    profile_name: str
    profile_description: Optional[str] = None
    ip_range: str
    last_scan: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProfileRead(BaseModel):
    profile_id: str
    profile_name: str
    profile_description: Optional[str] = None
    ip_range: str
    last_scan: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    scan_events: List["ScanEventRead"] = []

    class Config:
        from_attributes = True


class ScanEventRead(BaseModel):
    scan_id: int
    profile_id: str
    scan_command: str
    scan_start: datetime
    scan_end: datetime
    scan_status: str
    created_at: datetime

    class Config:
        from_attributes = True


class ProfileBaseSchema(BaseModel):
    profile_id: str | None = None
    profile_name: str
    ip_range: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

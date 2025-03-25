import json
from datetime import datetime
from typing import Any

from pydantic import BaseModel, field_validator


class Project(BaseModel):
    """Project model."""

    id: str
    name: str
    description: str | None = None
    team_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    metadata: dict[str, Any] | None = None


class DataSource(BaseModel):
    """Data source model."""

    id: str
    name: str
    type: str | None = None
    uri: str | None = None
    project_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    metadata: dict[str, Any] | None = None


class DataLine(BaseModel):
    """Data line model."""

    id: str
    name: str
    dataobject_id: str | None = None
    schema_code: str | None = None
    project_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    data_model: dict[str, Any] | None = None

    @field_validator("data_model", mode="before")
    @classmethod
    def parse_data_model(cls, v):
        """Parse data_model if it's a JSON string."""
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return None
        return v


class Team(BaseModel):
    """Team model."""

    id: str
    name: str
    organization_id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    metadata: dict[str, Any] | None = None


class Organization(BaseModel):
    """Organization model."""

    id: str
    name: str
    description: str | None = None
    platform_id: str | None = None
    clerk_org_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    metadata: dict[str, Any] | None = None


class User(BaseModel):
    """User model."""

    id: str
    email: str
    name: str | None = None
    organization_id: str | None = None
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    metadata: dict[str, Any] | None = None


class QueryProgram(BaseModel):
    """Query program model."""

    id: str
    name: str | None = None
    query: str | None = None
    query_program: str | None = None
    dataline_id: str | None = None
    project_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    published: bool | None = False
    public: bool | None = False
    metadata: dict[str, Any] | None = None
    steps: str | None = None
    slots: str | None = None
    stores: str | None = None
    reason: str | None = None
    prev_id: str | None = None
    ontologyId: str | None = None


class Secret(BaseModel):
    """Secret model."""

    id: str | None = None
    name: str
    value: str | None = None
    type: str | None = None
    description: str | None = None
    team_id: str
    credentials_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None
    metadata: dict[str, Any] | None = None


class Credential(BaseModel):
    """Credential model."""

    id: str
    name: str
    type: str
    organization_id: str | None = None
    team_id: str | None = None
    datasource_id: str | None = None
    infrastructure_id: str | None = None
    metadata: dict[str, Any] | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None


class TeamMembership(BaseModel):
    """Team membership model."""

    user_id: str
    team_id: str
    role: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    deleted_at: datetime | None = None

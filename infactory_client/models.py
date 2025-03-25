from typing import Dict, List, Optional, Union, Any
from datetime import datetime
from pydantic import BaseModel, Field


class Project(BaseModel):
    """Project model."""
    
    id: str
    name: str
    description: Optional[str] = None
    team_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class DataSource(BaseModel):
    """Data source model."""
    
    id: str
    name: str
    type: Optional[str] = None
    uri: Optional[str] = None
    project_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class DataLine(BaseModel):
    """Data line model."""
    
    id: str
    name: str
    dataobject_id: Optional[str] = None
    schema_code: Optional[str] = None
    project_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    data_model: Optional[Dict[str, Any]] = None


class Team(BaseModel):
    """Team model."""
    
    id: str
    name: str
    organization_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class Organization(BaseModel):
    """Organization model."""
    
    id: str
    name: str
    description: Optional[str] = None
    platform_id: Optional[str] = None
    clerk_org_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class User(BaseModel):
    """User model."""
    
    id: str
    email: str
    name: Optional[str] = None
    organization_id: Optional[str] = None
    role: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class QueryProgram(BaseModel):
    """Query program model."""
    
    id: str
    name: Optional[str] = None
    question: Optional[str] = None
    code: Optional[str] = None
    dataline_id: Optional[str] = None
    project_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    published: Optional[bool] = False
    public: Optional[bool] = False
    metadata: Optional[Dict[str, Any]] = None


class Secret(BaseModel):
    """Secret model."""
    
    id: Optional[str] = None
    name: str
    value: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    team_id: str
    credentials_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class Credential(BaseModel):
    """Credential model."""
    
    id: str
    name: str
    type: str
    organization_id: Optional[str] = None
    team_id: Optional[str] = None
    datasource_id: Optional[str] = None
    infrastructure_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


class TeamMembership(BaseModel):
    """Team membership model."""
    
    user_id: str
    team_id: str
    role: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

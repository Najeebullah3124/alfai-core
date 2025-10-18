"""
CMS - Content Models
Data structures for content management
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum

class ContentType(Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    DATA = "data"

class ContentStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"
    DELETED = "deleted"

@dataclass
class ContentItem:
    content_id: str
    title: str
    content_type: ContentType
    content_data: Any
    status: ContentStatus
    created_at: datetime
    updated_at: datetime
    metadata: Dict[str, Any]

@dataclass
class ContentVersion:
    version_id: str
    content_id: str
    version_number: int
    content_data: Any
    created_at: datetime
    author: str
    changes: List[str]

@dataclass
class ContentMetadata:
    content_id: str
    tags: List[str]
    categories: List[str]
    language: str
    quality_score: float
    accessibility_score: float
    seo_score: float

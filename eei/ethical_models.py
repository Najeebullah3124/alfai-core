"""
EEI - Ethical Models
Data structures for ethical evaluation
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum

class EthicalPrinciple(Enum):
    AUTONOMY = "autonomy"
    BENEFICENCE = "beneficence"
    NON_MALEFICENCE = "non_maleficence"
    JUSTICE = "justice"
    TRANSPARENCY = "transparency"
    ACCOUNTABILITY = "accountability"
    PRIVACY = "privacy"
    FAIRNESS = "fairness"

class ViolationSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class EthicalViolation:
    violation_id: str
    principle: EthicalPrinciple
    severity: ViolationSeverity
    description: str
    evidence: List[str]
    recommendations: List[str]
    timestamp: datetime

@dataclass
class EthicalAssessment:
    assessment_id: str
    overall_score: float
    principle_scores: Dict[str, float]
    violations: List[EthicalViolation]
    recommendations: List[str]
    timestamp: datetime

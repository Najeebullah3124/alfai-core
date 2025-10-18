"""
CCE - Compliance Models
Data structures for compliance checking
"""

from dataclasses import dataclass
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum

class ComplianceStandard(Enum):
    GDPR = "gdpr"
    CCPA = "ccpa"
    HIPAA = "hipaa"
    SOX = "sox"
    PCI_DSS = "pci_dss"
    ISO27001 = "iso27001"
    NIST = "nist"
    ADA = "ada"

class ViolationSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class ComplianceRule:
    rule_id: str
    standard: ComplianceStandard
    rule_name: str
    description: str
    severity: ViolationSeverity
    requirements: List[str]
    controls: List[str]

@dataclass
class ComplianceViolation:
    violation_id: str
    rule_id: str
    severity: ViolationSeverity
    description: str
    evidence: List[str]
    remediation: List[str]
    timestamp: datetime

@dataclass
class ComplianceCheck:
    check_id: str
    standard: ComplianceStandard
    overall_score: float
    violations: List[ComplianceViolation]
    recommendations: List[str]
    timestamp: datetime

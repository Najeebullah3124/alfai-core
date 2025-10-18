"""
AlfAI Core - Advanced AI Framework
14-Layer Architecture with Sub-modules: DRE, CMS, EEI, CCE
"""

from .layers.layer_framework import LayerFramework
from .dre import DRE
from .cms import CMS
from .eei import EEI
from .cce import CCE
from .api.alfai_api import AlfAIAPI
from .utils.flow_manager import FlowManager

__version__ = "1.0.0"
__author__ = "AlfAI Core Team"
__description__ = "Advanced AI Framework with 14-Layer Architecture"

__all__ = [
    "LayerFramework",
    "DRE",
    "CMS", 
    "EEI",
    "CCE",
    "AlfAIAPI",
    "FlowManager"
]

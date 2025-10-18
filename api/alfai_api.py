"""
AlfAI Core API
Main API interface for the AlfAI Core system
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import json
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ..layers.layer_framework import LayerFramework
from ..dre import DREEngine
from ..cms import CMSEngine
from ..eei import EEIEngine
from ..cce import CCEEngine
from ..utils.flow_manager import FlowManager

# Pydantic models for API
class PromptRequest(BaseModel):
    prompt: str
    context: Optional[Dict[str, Any]] = None
    user_id: Optional[str] = None

class PromptResponse(BaseModel):
    response: str
    processing_time_ms: int
    layer_results: Dict[str, Any]
    timestamp: datetime

class SupervisionRequest(BaseModel):
    data: Dict[str, Any]
    supervision_type: str
    user_id: Optional[str] = None

class SupervisionResponse(BaseModel):
    supervision_result: Dict[str, Any]
    processing_time_ms: int
    timestamp: datetime

class ReasoningRequest(BaseModel):
    data: Dict[str, Any]
    reasoning_type: str
    user_id: Optional[str] = None

class ReasoningResponse(BaseModel):
    reasoning_result: Dict[str, Any]
    processing_time_ms: int
    timestamp: datetime

class AuditRequest(BaseModel):
    data: Dict[str, Any]
    audit_type: str
    user_id: Optional[str] = None

class AuditResponse(BaseModel):
    audit_result: Dict[str, Any]
    processing_time_ms: int
    timestamp: datetime

# Initialize FastAPI app
app = FastAPI(
    title="AlfAI Core API",
    description="Advanced AI Framework with 14-Layer Architecture",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
layer_framework = LayerFramework()
dre_engine = DREEngine()
cms_engine = CMSEngine()
eei_engine = EEIEngine()
cce_engine = CCEEngine()
flow_manager = FlowManager()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "AlfAI Core API is running!",
        "version": "1.0.0",
        "architecture": "14-Layer Framework",
        "sub_modules": ["DRE", "CMS", "EEI", "CCE"],
        "status": "active"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "components": {
            "layer_framework": "active",
            "dre_engine": "active",
            "cms_engine": "active",
            "eei_engine": "active",
            "cce_engine": "active",
            "flow_manager": "active"
        }
    }

@app.post("/api/prompt", response_model=PromptResponse)
async def process_prompt(request: PromptRequest):
    """Process prompt through 14-layer framework"""
    start_time = datetime.utcnow()
    
    try:
        # Prepare input data
        input_data = {
            "prompt": request.prompt,
            "context": request.context or {},
            "user_id": request.user_id,
            "timestamp": start_time.isoformat()
        }
        
        # Process through 14 layers
        layer_results = layer_framework.process_through_layers(input_data)
        
        # Generate response
        response = f"Processed prompt through 14 layers: {request.prompt[:50]}..."
        
        processing_time = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        return PromptResponse(
            response=response,
            processing_time_ms=processing_time,
            layer_results=layer_results,
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/supervision", response_model=SupervisionResponse)
async def process_supervision(request: SupervisionRequest):
    """Process supervision through AXA-I integration"""
    start_time = datetime.utcnow()
    
    try:
        # Process through supervision components
        supervision_result = flow_manager.process_supervision(
            request.data,
            request.supervision_type,
            request.user_id
        )
        
        processing_time = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        return SupervisionResponse(
            supervision_result=supervision_result,
            processing_time_ms=processing_time,
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/reasoning", response_model=ReasoningResponse)
async def process_reasoning(request: ReasoningRequest):
    """Process reasoning through DRE engine"""
    start_time = datetime.utcnow()
    
    try:
        # Process through DRE engine
        reasoning_result = dre_engine.analyze_data(request.data)
        
        processing_time = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        return ReasoningResponse(
            reasoning_result=reasoning_result,
            processing_time_ms=processing_time,
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/audit", response_model=AuditResponse)
async def process_audit(request: AuditRequest):
    """Process audit through EEI and CCE engines"""
    start_time = datetime.utcnow()
    
    try:
        # Process through EEI and CCE engines
        eei_result = eei_engine.evaluate_ethics(request.data)
        cce_result = cce_engine.check_compliance(request.data)
        
        audit_result = {
            "eei_evaluation": eei_result,
            "cce_compliance": cce_result,
            "audit_timestamp": datetime.utcnow().isoformat()
        }
        
        processing_time = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        return AuditResponse(
            audit_result=audit_result,
            processing_time_ms=processing_time,
            timestamp=datetime.utcnow()
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/layers/status")
async def get_layer_status():
    """Get status of all 14 layers"""
    return {
        "total_layers": 14,
        "layer_status": [layer_framework.get_layer_status(i) for i in range(1, 15)],
        "framework_summary": layer_framework.get_processing_summary()
    }

@app.get("/api/modules/summary")
async def get_modules_summary():
    """Get summary of all sub-modules"""
    return {
        "dre_summary": dre_engine.get_reasoning_summary(),
        "cms_summary": cms_engine.get_content_summary(),
        "eei_summary": eei_engine.get_ethical_summary(),
        "cce_summary": cce_engine.get_compliance_summary()
    }

@app.post("/api/test/flow")
async def test_complete_flow():
    """Test complete flow: prompt → supervision → reasoning → audit"""
    start_time = datetime.utcnow()
    
    try:
        # Test data
        test_data = {
            "prompt": "Test AI decision making",
            "data": {"test": "data", "personal_data": "sample"},
            "user_id": "test_user"
        }
        
        # Step 1: Process prompt
        prompt_result = layer_framework.process_through_layers(test_data)
        
        # Step 2: Supervision
        supervision_result = flow_manager.process_supervision(
            test_data, "test_supervision", "test_user"
        )
        
        # Step 3: Reasoning
        reasoning_result = dre_engine.analyze_data(test_data)
        
        # Step 4: Audit
        eei_result = eei_engine.evaluate_ethics(test_data)
        cce_result = cce_engine.check_compliance(test_data)
        
        total_time = int((datetime.utcnow() - start_time).total_seconds() * 1000)
        
        return {
            "test_completed": True,
            "total_processing_time_ms": total_time,
            "results": {
                "prompt_processing": prompt_result,
                "supervision": supervision_result,
                "reasoning": reasoning_result,
                "audit": {
                    "eei": eei_result,
                    "cce": cce_result
                }
            },
            "timestamp": datetime.utcnow().isoformat()
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

# AlfAI Core - API Map

## 🗺️ **API Architecture Overview**

```
┌─────────────────────────────────────────────────────────────────┐
│                        AlfAI Core API                           │
│                     (Port: 8001)                                │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Core Endpoints                               │
├─────────────────────────────────────────────────────────────────┤
│  GET  /                    │ Root endpoint                     │
│  GET  /health              │ Health check                     │
│  GET  /docs                │ API documentation                │
│  GET  /redoc               │ Alternative docs                 │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Processing Endpoints                         │
├─────────────────────────────────────────────────────────────────┤
│  POST /api/prompt           │ 14-Layer Framework Processing     │
│  POST /api/supervision     │ AXA-I Supervision                 │
│  POST /api/reasoning       │ DRE Engine Analysis               │
│  POST /api/audit           │ EEI + CCE Audit                  │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Status Endpoints                             │
├─────────────────────────────────────────────────────────────────┤
│  GET  /api/layers/status   │ 14-Layer Status                  │
│  GET  /api/modules/summary │ Sub-module Summaries             │
│  POST /api/test/flow       │ Complete Flow Test                │
└─────────────────────────────────────────────────────────────────┘
```

## 📋 **Detailed API Endpoints**

### **Core System Endpoints**

#### **GET /**
- **Purpose**: Root endpoint with system information
- **Response**: System status, version, architecture details
- **Example**:
```json
{
  "message": "AlfAI Core API is running!",
  "version": "1.0.0",
  "architecture": "14-Layer Framework",
  "sub_modules": ["DRE", "CMS", "EEI", "CCE"],
  "status": "active"
}
```

#### **GET /health**
- **Purpose**: Health check for all components
- **Response**: Component status and system health
- **Example**:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "components": {
    "layer_framework": "active",
    "dre_engine": "active",
    "cms_engine": "active",
    "eei_engine": "active",
    "cce_engine": "active",
    "flow_manager": "active"
  }
}
```

### **Processing Endpoints**

#### **POST /api/prompt**
- **Purpose**: Process prompts through 14-layer framework
- **Request Body**:
```json
{
  "prompt": "Analyze customer data for loan approval",
  "context": {
    "user_id": "user_123",
    "session_id": "sess_456"
  },
  "user_id": "user_123"
}
```
- **Response**:
```json
{
  "response": "Processed prompt through 14 layers...",
  "processing_time_ms": 150,
  "layer_results": {
    "final_result": {...},
    "processing_log": [...],
    "total_layers": 14,
    "successful_layers": 14
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### **POST /api/supervision**
- **Purpose**: Process supervision through AXA-I integration
- **Request Body**:
```json
{
  "data": {
    "customer_data": {...},
    "decision_context": "loan_approval"
  },
  "supervision_type": "loan_approval_supervision",
  "user_id": "user_123"
}
```
- **Response**:
```json
{
  "supervision_result": {
    "supervision_type": "loan_approval_supervision",
    "axa_i_processing": {
      "validation_completed": true,
      "bias_detection_completed": true,
      "legality_verification_completed": true,
      "decision_recorded": true
    },
    "supervision_score": 0.85,
    "recommendations": [...]
  },
  "processing_time_ms": 200,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### **POST /api/reasoning**
- **Purpose**: Process reasoning through DRE engine
- **Request Body**:
```json
{
  "data": {
    "customer_data": {...},
    "analysis_type": "loan_risk_assessment"
  },
  "reasoning_type": "inductive",
  "user_id": "user_123"
}
```
- **Response**:
```json
{
  "reasoning_result": {
    "dre_analysis": {
      "patterns_detected": 3,
      "inferences_generated": 2,
      "confidence_score": 0.85
    },
    "patterns": [...],
    "inferences": [...]
  },
  "processing_time_ms": 100,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### **POST /api/audit**
- **Purpose**: Process audit through EEI + CCE engines
- **Request Body**:
```json
{
  "data": {
    "customer_data": {...},
    "decision_data": {...}
  },
  "audit_type": "comprehensive_audit",
  "user_id": "user_123"
}
```
- **Response**:
```json
{
  "audit_result": {
    "eei_evaluation": {
      "overall_score": 0.92,
      "violations_detected": 0,
      "ethical_compliance": true
    },
    "cce_compliance": {
      "overall_score": 0.88,
      "standards_checked": ["GDPR", "CCPA", "ADA"],
      "total_violations": 0,
      "compliance_status": "compliant"
    }
  },
  "processing_time_ms": 300,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### **Status Endpoints**

#### **GET /api/layers/status**
- **Purpose**: Get status of all 14 layers
- **Response**:
```json
{
  "total_layers": 14,
  "layer_status": [
    {
      "layer_id": 1,
      "name": "Input Interface",
      "status": "completed",
      "processing_time_ms": 5,
      "timestamp": "2024-01-15T10:30:00Z"
    },
    ...
  ],
  "framework_summary": {
    "total_layers": 14,
    "success_rate": 1.0,
    "total_processing_time": 150,
    "framework_status": "active"
  }
}
```

#### **GET /api/modules/summary**
- **Purpose**: Get summary of all sub-modules
- **Response**:
```json
{
  "dre_summary": {
    "total_patterns": 5,
    "total_inferences": 3,
    "average_confidence": 0.85,
    "engine_status": "active"
  },
  "cms_summary": {
    "total_content_items": 10,
    "content_types": ["text", "data"],
    "average_quality_score": 0.88,
    "cms_status": "active"
  },
  "eei_summary": {
    "total_assessments": 8,
    "ethical_principles": ["autonomy", "beneficence", ...],
    "average_ethical_score": 0.92,
    "eei_status": "active"
  },
  "cce_summary": {
    "total_checks": 12,
    "compliance_standards": ["GDPR", "CCPA", ...],
    "average_compliance_score": 0.88,
    "cce_status": "active"
  }
}
```

#### **POST /api/test/flow**
- **Purpose**: Test complete flow: prompt → supervision → reasoning → audit
- **Response**:
```json
{
  "test_completed": true,
  "total_processing_time_ms": 750,
  "results": {
    "prompt_processing": {...},
    "supervision": {...},
    "reasoning": {...},
    "audit": {...}
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## 🔄 **API Flow Diagram**

```
Client Request
     │
     ▼
┌─────────────────┐
│   API Gateway   │
│   (FastAPI)     │
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  Route Handler  │
│  (Endpoint)     │
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  Layer Framework│
│  (14 Layers)    │
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  Sub-modules    │
│  (DRE/CMS/EEI/CCE)│
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  Flow Manager   │
│  (AXA-I/MFE)    │
└─────────────────┘
     │
     ▼
┌─────────────────┐
│  Response       │
│  (JSON)         │
└─────────────────┘
```

## 📊 **Performance Metrics**

### **Response Times**
- **Root Endpoint**: < 10ms
- **Health Check**: < 20ms
- **Prompt Processing**: 100-200ms
- **Supervision**: 150-300ms
- **Reasoning**: 50-150ms
- **Audit**: 200-400ms
- **Complete Flow**: 500-1000ms

### **Throughput**
- **Concurrent Requests**: 100+ requests/second
- **Layer Processing**: 1000+ layers/second
- **Component Integration**: 500+ operations/second

## 🔒 **Security Features**

### **Authentication**
- **API Key Authentication**: Secure API access
- **Rate Limiting**: Request throttling
- **CORS Configuration**: Cross-origin security

### **Data Protection**
- **Input Validation**: Pydantic model validation
- **Error Handling**: Comprehensive exception management
- **Logging**: Complete request/response logging

## 🚀 **Deployment**

### **Local Development**
```bash
# Start the API server
python api/alfai_api.py

# Access the API
curl http://localhost:8001/
```

### **Production Deployment**
```bash
# Using uvicorn
uvicorn api.alfai_api:app --host 0.0.0.0 --port 8001

# Using Docker
docker run -p 8001:8001 alfai-core
```

### **API Documentation**
- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc
- **OpenAPI Schema**: http://localhost:8001/openapi.json

## 📈 **Monitoring**

### **Health Monitoring**
- **Component Status**: Real-time component health
- **Performance Metrics**: Response times and throughput
- **Error Tracking**: Exception monitoring and logging

### **Analytics**
- **Usage Statistics**: API endpoint usage
- **Performance Trends**: Response time trends
- **Error Rates**: Error frequency and types

---

**AlfAI Core API** - Advanced AI Framework API
*Comprehensive RESTful API for 14-layer AI processing*
